"""Document Internal Consistency Score (DICS).

This is **not** a true coreference model. Repeated mentions of the same entity
type may refer to different real-world referents (e.g. two doctor names). We
therefore score only identity-bearing types that must be unique within a
document, and report multi-value types as ``multi_referent`` rather than as
hard conflicts.
"""

from __future__ import annotations

from collections import defaultdict

from main.entities.inline import extract_inline_spans

# Types that should have a single surface form per document when repeated.
# Other types may legitimately have multiple distinct values (different people,
# facilities, addresses) and are tracked separately — not as DICS failures.
IDENTITY_ENTITY_TYPES: frozenset[str] = frozenset(
    {
        "AADHAAR_NUMBER",
        "PAN_NUMBER",
        "ABHA_ID",
        "ABHA_ADDRESS",
        "MRN",
        "PATIENT_ID",
        "PATIENT_NAME",
        "DOB",
        "PHONE_NUMBER",
        "EMAIL_ADDRESS",
        "BANK_ACCOUNT_NUMBER",
        "CREDIT_CARD_NUMBER",
        "PASSPORT_NUMBER",
        "DRIVING_LICENCE",
        "VOTER_ID",
        "INSURANCE_POLICY_NUMBER",
        "ADMISSION_NUMBER",
        "ENCOUNTER_ID",
        "IMEI_NUMBER",
        "MAC_ADDRESS",
        "IP_ADDRESS",
        "VEHICLE_REGISTRATION",
    }
)


def compute_dics(text: str) -> dict[str, object]:
    """DICS over identity types only.

    For each identity entity type that appears more than once, all values must
    match. Multi-referent types (e.g. DOCTOR_NAME, HOSPITAL_NAME) are reported
    but do not reduce the score.
    """
    by_type: dict[str, list[str]] = defaultdict(list)
    for span in extract_inline_spans(text):
        by_type[span.entity_type].append(span.value.strip())

    total = 0
    consistent = 0
    conflicts: dict[str, list[str]] = {}
    multi_referent: dict[str, list[str]] = {}

    for entity_type, values in by_type.items():
        if len(values) < 2:
            continue
        unique = sorted(set(values))
        if entity_type not in IDENTITY_ENTITY_TYPES:
            if len(unique) > 1:
                multi_referent[entity_type] = unique
            continue
        total += len(values)
        if len(unique) == 1:
            consistent += len(values)
        else:
            conflicts[entity_type] = unique

    score = 1.0 if total == 0 else consistent / total
    return {
        "dics": score,
        "coreference_mentions": total,
        "consistent_mentions": consistent,
        "conflicts": conflicts,
        "multi_referent": multi_referent,
        "identity_entity_types": sorted(IDENTITY_ENTITY_TYPES),
        "model": "identity_type_uniqueness_not_coreference",
        "ok": score == 1.0,
    }
