"""Indic-plausible surrogate helpers used by validators / future generators."""

from __future__ import annotations

import hashlib
import re


_AADHAAR_RE = re.compile(r"^\d{12}$")
_PAN_RE = re.compile(r"^[A-Z]{5}\d{4}[A-Z]$")
_IFSC_RE = re.compile(r"^[A-Z]{4}0[A-Z0-9]{6}$")
_PIN_RE = re.compile(r"^[1-9]\d{5}$")
_PHONE_RE = re.compile(r"^(?:\+?91[\-\s]?)?[6-9]\d{9}$")


def normalize_digits(value: str) -> str:
    return re.sub(r"\D", "", value)


def looks_like_aadhaar(value: str) -> bool:
    return bool(_AADHAAR_RE.fullmatch(normalize_digits(value)))


def looks_like_pan(value: str) -> bool:
    return bool(_PAN_RE.fullmatch(value.strip().upper()))


def looks_like_ifsc(value: str) -> bool:
    return bool(_IFSC_RE.fullmatch(value.strip().upper()))


def looks_like_pin(value: str) -> bool:
    return bool(_PIN_RE.fullmatch(normalize_digits(value)))


def looks_like_phone(value: str) -> bool:
    compact = re.sub(r"[\s\-()]", "", value.strip())
    return bool(_PHONE_RE.fullmatch(compact))


def stable_bucket(seed: str, modulus: int) -> int:
    digest = hashlib.blake2b(seed.encode("utf-8"), digest_size=8).digest()
    return int.from_bytes(digest, "big") % modulus
