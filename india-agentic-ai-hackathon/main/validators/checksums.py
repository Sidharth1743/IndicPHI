"""Checksum and format validators for Indian identifiers."""

from __future__ import annotations

from main.entities.surrogate import (
    looks_like_aadhaar,
    looks_like_ifsc,
    looks_like_pan,
    looks_like_phone,
    looks_like_pin,
    normalize_digits,
)

_VERHOEFF_D = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 2, 3, 4, 0, 6, 7, 8, 9, 5),
    (2, 3, 4, 0, 1, 7, 8, 9, 5, 6),
    (3, 4, 0, 1, 2, 8, 9, 5, 6, 7),
    (4, 0, 1, 2, 3, 9, 5, 6, 7, 8),
    (5, 9, 8, 7, 6, 0, 4, 3, 2, 1),
    (6, 5, 9, 8, 7, 1, 0, 4, 3, 2),
    (7, 6, 5, 9, 8, 2, 1, 0, 4, 3),
    (8, 7, 6, 5, 9, 3, 2, 1, 0, 4),
    (9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
)
_VERHOEFF_P = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 5, 7, 6, 2, 8, 3, 0, 9, 4),
    (5, 8, 0, 3, 7, 9, 6, 1, 4, 2),
    (8, 9, 1, 6, 0, 4, 3, 5, 2, 7),
    (9, 4, 5, 3, 1, 2, 6, 8, 7, 0),
    (4, 2, 8, 6, 5, 7, 3, 9, 0, 1),
    (2, 7, 9, 3, 8, 0, 6, 4, 1, 5),
    (7, 0, 4, 6, 9, 1, 3, 2, 5, 8),
)


def verhoeff_validate(number: str) -> bool:
    digits = normalize_digits(number)
    if not digits:
        return False
    checksum = 0
    for index, char in enumerate(reversed(digits)):
        checksum = _VERHOEFF_D[checksum][_VERHOEFF_P[index % 8][int(char)]]
    return checksum == 0


def validate_aadhaar(value: str) -> tuple[bool, str]:
    digits = normalize_digits(value)
    if not looks_like_aadhaar(digits):
        return False, "aadhaar_format"
    if digits[0] in {"0", "1"}:
        return False, "aadhaar_leading_digit"
    if not verhoeff_validate(digits):
        return False, "aadhaar_verhoeff"
    return True, "ok"


def validate_pan(value: str) -> tuple[bool, str]:
    if not looks_like_pan(value):
        return False, "pan_format"
    return True, "ok"


def validate_ifsc(value: str) -> tuple[bool, str]:
    if not looks_like_ifsc(value):
        return False, "ifsc_format"
    return True, "ok"


def validate_pin(value: str) -> tuple[bool, str]:
    digits = normalize_digits(value)
    if not looks_like_pin(digits):
        return False, "pin_format"
    return True, "ok"


def validate_phone(value: str) -> tuple[bool, str]:
    if not looks_like_phone(value):
        return False, "phone_format"
    return True, "ok"


_ENTITY_VALIDATORS = {
    "AADHAAR_NUMBER": validate_aadhaar,
    "PAN_NUMBER": validate_pan,
    "IFSC_CODE": validate_ifsc,
    "PIN_CODE": validate_pin,
    "PHONE_NUMBER": validate_phone,
}


def validate_entity_value(entity_type: str, value: str) -> tuple[bool, str]:
    validator = _ENTITY_VALIDATORS.get(entity_type)
    if validator is None:
        return True, "no_format_check"
    return validator(value)
