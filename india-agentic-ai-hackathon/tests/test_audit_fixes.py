"""Unit tests for audit-driven pipeline hardening."""

from __future__ import annotations

from pathlib import Path

from main.designers.translator import protect_tags, restore_tags
from main.pipeline.checkpoint import CheckpointStore, request_hash
from main.pipeline.semantic_dedup import find_semantic_near_duplicates
from main.validators.dics import compute_dics
from main.validators.phi_residue import scan_phi_residue


def test_protect_tags_separates_id_from_names() -> None:
    text = (
        "Patient [[PATIENT_NAME|Ravi Kumar]] Aadhaar [[AADHAAR_NUMBER|1234 5678 9012]] "
        "lives at [[RESIDENTIAL_ADDRESS|12 MG Road]]."
    )
    prot = protect_tags(text)
    assert "⟦ID0⟧" in prot.text
    assert "[[PATIENT_NAME|⟦NM0⟧]]" in prot.text
    assert "[[RESIDENTIAL_ADDRESS|⟦NM1⟧]]" in prot.text
    # ID value must not appear as free text in the protected payload.
    assert "1234 5678 9012" not in prot.text
    # Name values are placeholder-locked (TYPE stays visible for the model).
    assert "Ravi Kumar" not in prot.text
    # Simulate model translating name placeholders' values by rewriting tags.
    translated = (
        prot.text.replace("⟦NM0⟧", "रवि कुमार").replace("⟦NM1⟧", "१२ एमजी रोड")
    )
    restored = restore_tags(translated, prot)
    assert "[[AADHAAR_NUMBER|1234 5678 9012]]" in restored
    assert "[[PATIENT_NAME|रवि कुमार]]" in restored
    assert "[[RESIDENTIAL_ADDRESS|१२ एमजी रोड]]" in restored



def test_dics_allows_multi_referent_doctor_names() -> None:
    text = (
        "Seen by [[DOCTOR_NAME|Dr A]] then [[DOCTOR_NAME|Dr B]]. "
        "Patient [[PATIENT_NAME|X]] aka [[PATIENT_NAME|X]]."
    )
    report = compute_dics(text)
    assert report["ok"] is True
    assert "DOCTOR_NAME" in report["multi_referent"]
    assert report["dics"] == 1.0


def test_dics_flags_identity_conflict() -> None:
    text = "[[AADHAAR_NUMBER|1111 2222 3333]] then [[AADHAAR_NUMBER|9999 8888 7777]]"
    report = compute_dics(text)
    assert report["ok"] is False
    assert "AADHAAR_NUMBER" in report["conflicts"]


def test_phi_residue_covers_extended_families() -> None:
    text = (
        "Contact 9876543210 email a@b.com MRN-12345 passport A1234567 "
        "http://example.com mac AA:BB:CC:DD:EE:FF ip 10.0.0.1 "
        "card 4111 1111 1111 1111 abha 12-3456-7890-1234"
    )
    hits = scan_phi_residue(text)
    kinds = {h["kind"] for h in hits}
    for expected in (
        "phone_like",
        "email_like",
        "mrn_like",
        "passport_like",
        "url_like",
        "mac_like",
        "ipv4_like",
        "credit_card_like",
        "abha_like",
    ):
        assert expected in kinds, f"missing {expected} in {kinds}"


def test_checkpoint_resume(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "checkpoint.jsonl")
    req = request_hash(["a", 1])
    store.append(row_key="u__0", status="ok", request_hash=req, payload={"v": 1})
    store2 = CheckpointStore(tmp_path / "checkpoint.jsonl")
    assert "u__0" in store2.done_keys()
    assert store2.get("u__0").payload["v"] == 1


def test_semantic_dedup_drops_near_copies() -> None:
    docs = [
        ("a", "Patient admitted with fever and cough after travel."),
        ("b", "Patient admitted with fever and cough after travel."),
        ("c", "Completely different surgical note about fracture repair."),
    ]
    drop, report = find_semantic_near_duplicates(docs, threshold=0.95)
    assert "b" in drop
    assert "c" not in drop
    assert report["dropped"] >= 1
