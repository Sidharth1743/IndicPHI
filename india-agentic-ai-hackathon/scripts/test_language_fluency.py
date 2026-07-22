#!/usr/bin/env python3
"""Fluency probe: ask each model for 5–6 lines per languages.yaml language.

Writes all model×language samples into a single markdown file under results/.
No scoring / script-purity checks — raw generations only.

Usage (from india-agentic-ai-hackathon/):
  .venv/bin/python scripts/test_language_fluency.py
  .venv/bin/python scripts/test_language_fluency.py --models sarvam-105b,grok-4.3
  .venv/bin/python scripts/test_language_fluency.py --codes hi,ta,en
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Protocol

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from main.llm.openai_compatible import (
    OpenAICompatibleClient,
    OpenAICompatibleClientError,
)
from main.llm.rate_limit import RateLimiter
from main.llm.sarvam import SarvamClient, SarvamClientError
from main.pipeline.env import load_env_file, require_env

DEFAULT_MODELS = ("sarvam-30b", "sarvam-105b", "grok-4.3")
DEFAULT_LANGUAGES = REPO_ROOT / "configs" / "synthetic-data" / "languages.yaml"
DEFAULT_SARVAM_BASE_URL = "https://api.sarvam.ai/v1"
DEFAULT_GROK_BASE_URL = (
    "https://ambedkar-interpreter-resource.services.ai.azure.com/openai/v1"
)
GROK_MODELS = frozenset({"grok-4.3", "grok"})


class _ChatClient(Protocol):
    def chat_completion(self, **kwargs): ...


def _load_languages(path: Path, codes: set[str] | None) -> list[dict]:
    root = yaml.safe_load(path.read_text(encoding="utf-8"))
    languages = root.get("languages")
    if not isinstance(languages, list) or not languages:
        raise SystemExit(f"No languages found in {path}")
    out: list[dict] = []
    for item in languages:
        code = str(item["code"])
        if codes is not None and code not in codes:
            continue
        out.append(
            {
                "code": code,
                "name": str(item["name"]),
                "script": str(item["script"]),
            }
        )
    if not out:
        raise SystemExit("No languages selected after --codes filter")
    return out


def _is_grok(model: str) -> bool:
    return model in GROK_MODELS or model.startswith("grok")


def _prompt(lang: dict) -> list[dict[str, str]]:
    name = lang["name"]
    script = lang["script"]
    user = (
        f"Write exactly 5 or 6 short lines of natural, fluent {name} "
        f"in the {script} script.\n"
        f"Topic: a person describing a mild fever and visit to a local clinic.\n"
        f"Rules:\n"
        f"- Output ONLY the {name} lines (no English, no title, no numbering).\n"
        f"- Use the {script} script correctly.\n"
        f"- Keep each line one ordinary sentence."
    )
    return [
        {
            "role": "system",
            "content": (
                "You are a native writer. Reply with fluent target-language "
                "prose only. No translation notes."
            ),
        },
        {"role": "user", "content": user},
    ]


def _section(
    *,
    model: str,
    lang: dict,
    text: str,
    error: str | None,
    elapsed_s: float,
) -> str:
    lines = [
        f"## `{lang['code']}` — {lang['name']} ({lang['script']}) · model `{model}`",
        "",
        f"- elapsed_s: {elapsed_s:.1f}",
    ]
    if error:
        lines.extend([f"- status: ERROR", f"- error: {error}", ""])
        return "\n".join(lines)
    lines.extend(["- status: OK", "", "```text", text.strip(), "```", ""])
    return "\n".join(lines)


def _build_clients(
    *,
    models: list[str],
    sarvam_base_url: str,
    grok_base_url: str,
    requests_per_minute: float,
) -> dict[str, _ChatClient]:
    clients: dict[str, _ChatClient] = {}
    need_sarvam = any(not _is_grok(m) for m in models)
    need_grok = any(_is_grok(m) for m in models)

    if need_sarvam:
        sarvam = SarvamClient(
            api_key=require_env("SARVAM_API_KEY"),
            base_url=sarvam_base_url,
            rate_limiter=RateLimiter(requests_per_minute),
        )
        for model in models:
            if not _is_grok(model):
                clients[model] = sarvam

    if need_grok:
        grok_key = require_env(
            "AZURE_FOUNDRY_API_KEY",
            fallbacks=["AZURE_FOUNDARY_API_KEY"],
        )
        grok_url = (
            os.environ.get("AZURE_FOUNDRY_CHAT_BASE_URL", "").strip()
            or grok_base_url
        )
        # Grok judge account: 500 RPM; keep a conservative shared limiter.
        grok = OpenAICompatibleClient(
            api_key=grok_key,
            base_url=grok_url,
            rate_limiter=RateLimiter(min(requests_per_minute, 400.0)),
        )
        for model in models:
            if _is_grok(model):
                clients[model] = grok

    return clients


def _generate(
    client: _ChatClient,
    *,
    model: str,
    messages: list[dict[str, str]],
    temperature: float,
    max_tokens: int,
    timeout_s: float,
):
    if _is_grok(model):
        return client.chat_completion(
            model=model if model != "grok" else "grok-4.3",
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout_s=timeout_s,
        )
    return client.chat_completion(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        reasoning_effort=None,
        timeout_s=timeout_s,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--languages",
        type=Path,
        default=DEFAULT_LANGUAGES,
        help="Path to languages.yaml",
    )
    parser.add_argument(
        "--models",
        default=",".join(DEFAULT_MODELS),
        help="Comma-separated model ids (default: sarvam-30b,sarvam-105b,grok-4.3)",
    )
    parser.add_argument(
        "--codes",
        default="",
        help="Optional comma-separated language codes subset (e.g. hi,ta,en)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output markdown path (default: results/fluency_probe_<ts>.md)",
    )
    parser.add_argument("--sarvam-base-url", default=DEFAULT_SARVAM_BASE_URL)
    parser.add_argument("--grok-base-url", default=DEFAULT_GROK_BASE_URL)
    parser.add_argument("--temperature", type=float, default=0.3)
    parser.add_argument("--max-tokens", type=int, default=512)
    parser.add_argument("--requests-per-minute", type=float, default=110.0)
    parser.add_argument("--timeout-s", type=float, default=180.0)
    parser.add_argument(
        "--retries",
        type=int,
        default=0,
        help="Extra attempts per language on timeout/network errors",
    )
    args = parser.parse_args()

    load_env_file(REPO_ROOT / ".env")
    load_env_file(REPO_ROOT.parent / ".env")

    codes = {c.strip() for c in args.codes.split(",") if c.strip()} or None
    languages = _load_languages(args.languages, codes)
    models = [m.strip() for m in args.models.split(",") if m.strip()]
    if not models:
        raise SystemExit("No models specified")

    clients = _build_clients(
        models=models,
        sarvam_base_url=args.sarvam_base_url,
        grok_base_url=args.grok_base_url,
        requests_per_minute=args.requests_per_minute,
    )

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = args.output or (REPO_ROOT / "results" / f"fluency_probe_{ts}.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    header = [
        "# Language fluency probe",
        "",
        f"- started_utc: {ts}",
        f"- languages_config: `{args.languages}`",
        f"- language_count: {len(languages)}",
        f"- models: {', '.join(f'`{m}`' for m in models)}",
        f"- prompt: 5–6 fluent lines per language (clinic / mild fever)",
        "",
        "---",
        "",
    ]
    parts = ["\n".join(header)]
    ok_n = 0
    err_n = 0

    total = len(models) * len(languages)
    done = 0
    for model in models:
        client = clients[model]
        for lang in languages:
            done += 1
            label = f"[{done}/{total}] {model} · {lang['code']} ({lang['name']})"
            print(label, flush=True)
            t0 = time.monotonic()
            error: str | None = None
            text = ""
            attempts = max(1, 1 + int(args.retries))
            for attempt in range(1, attempts + 1):
                try:
                    result = _generate(
                        client,
                        model=model,
                        messages=_prompt(lang),
                        temperature=args.temperature,
                        max_tokens=args.max_tokens,
                        timeout_s=args.timeout_s,
                    )
                    text = result.content
                    error = None
                    ok_n += 1
                    print(
                        f"  OK attempt={attempt}/{attempts} "
                        f"({time.monotonic() - t0:.1f}s)",
                        flush=True,
                    )
                    break
                except (
                    SarvamClientError,
                    OpenAICompatibleClientError,
                    OSError,
                ) as exc:
                    error = str(exc)
                    print(
                        f"  ERROR attempt={attempt}/{attempts} {error[:200]}",
                        flush=True,
                    )
                    if attempt < attempts:
                        time.sleep(2.0 * attempt)
            if error is not None:
                err_n += 1

            parts.append(
                _section(
                    model=model,
                    lang=lang,
                    text=text,
                    error=error,
                    elapsed_s=time.monotonic() - t0,
                )
            )
            out_path.write_text("\n".join(parts), encoding="utf-8")

    summary = [
        "---",
        "",
        "# Summary",
        "",
        f"- ok: {ok_n}",
        f"- errors: {err_n}",
        f"- output: `{out_path}`",
        "",
    ]
    parts.append("\n".join(summary))
    out_path.write_text("\n".join(parts), encoding="utf-8")
    print(f"\nWrote {out_path}", flush=True)
    print(f"ok={ok_n} errors={err_n}", flush=True)
    return 1 if err_n else 0


if __name__ == "__main__":
    raise SystemExit(main())
