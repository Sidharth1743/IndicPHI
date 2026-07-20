"""Script purity + alias coverage for all 23 configured languages."""

from __future__ import annotations

from pathlib import Path

import yaml

from main.validators.script_purity import (
    evaluate_script_purity,
    normalize_script_name,
)

REPO = Path(__file__).resolve().parents[1]
LANG_YAML = REPO / "configs" / "synthetic-data" / "languages.yaml"

# Representative letters per script (enough for ratio checks).
_SCRIPT_SAMPLES: dict[str, str] = {
    "Latin": "Patient admitted with fever and cough.",
    "Devanagari": "रोगी को बुखार और खांसी है।",
    "Bengali": "রোগীর জ্বর এবং কাশি আছে।",
    "Gurmukhi": "ਮਰੀਜ਼ ਨੂੰ ਬੁਖਾਰ ਅਤੇ ਖੰਘ ਹੈ।",
    "Gujarati": "દર્દીને તાવ અને ઉધરસ છે.",
    "Odia": "ରୋଗୀଙ୍କୁ ଜ୍ୱର ଏବଂ କାଶ ଅଛି।",
    "Oriya": "ରୋଗୀଙ୍କୁ ଜ୍ୱର ଏବଂ କାଶ ଅଛି।",
    "Tamil": "நோயாளிக்கு காய்ச்சல் மற்றும் இருமல் உள்ளது.",
    "Telugu": "రోగికి జ్వరం మరియు దగ్గు ఉంది.",
    "Kannada": "ರೋಗಿಗೆ ಜ್ವರ ಮತ್ತು ಕೆಮ್ಮು ಇದೆ.",
    "Malayalam": "രോഗിക്ക് പനിയും ചുമയും ഉണ്ട്.",
    "Arabic": "المريض يعاني من الحمى والسعال.",
    "Meitei": "ꯄꯨꯛꯄ ꯑꯣꯏꯔꯤꯕ ꯃꯤꯑꯣꯏꯁꯤꯡꯒꯤ ꯑꯦꯛꯁꯤꯗꯦꯟꯇ ꯑꯃꯒꯤ ꯃꯇꯨꯡꯏꯟꯅ ꯂꯥꯏꯔꯤ꯫",
    "Ol Chiki": "ᱟᱹᱲᱤᱧ ᱠᱚᱨᱮ ᱵᱩᱠᱷᱟᱹᱨ ᱟᱨ ᱠᱷᱟᱸᱥᱤ ᱢᱮᱱᱟᱜᱼᱟ᱾",
}


def _load_languages() -> list[dict]:
    root = yaml.safe_load(LANG_YAML.read_text(encoding="utf-8"))
    languages = root["languages"]
    assert len(languages) == 23, f"expected 23 languages, got {len(languages)}"
    return languages


def test_all_23_languages_have_script_coverage() -> None:
    for spec in _load_languages():
        script = normalize_script_name(spec["script"])
        assert script in _SCRIPT_SAMPLES, (
            f"{spec['code']}: script {script!r} missing sample text"
        )
        sample = _SCRIPT_SAMPLES[script]
        ok, reason = evaluate_script_purity(
            sample,
            language_code=spec["code"],
            script=spec["script"],
        )
        assert ok, f"{spec['code']} ({script}) failed purity: {reason}"


def test_ol_chiki_alias_normalizes() -> None:
    assert normalize_script_name("Ol_Chiki") == "Ol Chiki"
    ok, reason = evaluate_script_purity(
        _SCRIPT_SAMPLES["Ol Chiki"],
        language_code="sat",
        script="Ol_Chiki",
    )
    assert ok, reason


def test_wrong_indic_script_detected() -> None:
    # Gujarati doc body written in Devanagari should fail.
    ok, reason = evaluate_script_purity(
        _SCRIPT_SAMPLES["Devanagari"],
        language_code="gu",
        script="Gujarati",
    )
    assert not ok
    assert reason.startswith("wrong_indic_script:")
