from evidence import register_evidence
from evidence import get_evidence
from evidence import verify_evidence

original_file = b"This is original test evidence."
modified_file = b"This is modified test evidence."

print("*** EVIDENCE REGISTRATION TEST ***")

record = register_evidence("sample.txt", original_file)

evidence_id = record["evidence_id"]

print("\nRegistered evidence:")

for key, value in record.items():
    print(f"{key}: {value}")

print("\n*** RETRIEVAL TEST ***")

retrieved = get_evidence(evidence_id)

assert retrieved == record
print("Evidence retrieved successfully!")

print("\n*** VERIFICATION TEST ***")

print("Original file:", verify_evidence(
    evidence_id, original_file
))

print("Modified file:", verify_evidence(
    evidence_id, modified_file
))

assert verify_evidence(evidence_id, original_file)
assert not verify_evidence(evidence_id, modified_file)

print("\nAll registry tests passed!")
