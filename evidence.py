import hashlib
import json
import uuid
from pathlib import Path
from datetime import datetime, timezone

REGISTRY_FILE = Path(__file__).resolve().parent / "registry.json"

def calculate_hash(file_data):
	"""generate a SHA-256 hash of a file"""
	return hashlib.sha256(file_data).hexdigest()
	
def extract_metadata(filename, file_data):
	"""extract basic info about a file"""
	return{
		"filename": filename,
		"size_bytes": len(file_data),
		"file_extension": filename.rsplit(".", 1)[-1]
		if "." in filename else "unknown",
		"sha256": calculate_hash(file_data),
		"registered_at": datetime.now(timezone.utc).isoformat()
	}
	
def verify_integrity(file_data, original_hash):
	"""check whether a file matches its recorded hash"""
	current_hash = calculate_hash(file_data)
	return current_hash ==original_hash
	
def load_registry():
	"""load existing evidence records"""
	if not REGISTRY_FILE.exists():
		return{}
		
	with open(REGISTRY_FILE, "r") as file:
		return json.load(file)
		
def save_registry(registry):
	"""save evidence records to the JSON file"""
	with open(REGISTRY_FILE, "w") as file:
		json.dump(registry, file, indent=4)

def register_evidence(filename, file_data):
	"""register a new piece of digital evidence"""
	registry = load_registry()
	
	evidence_id = str(uuid.uuid4())
	metadata = extract_metadata(filename, file_data)
	metadata["evidence_id"] = evidence_id
	registry[evidence_id] = metadata
	save_registry(registry)
	return metadata
	
def get_evidence(evidence_id):
	"""retrieve using its unique ID"""
	registry = load_registry()
	return registry.get(evidence_id)
	
def verify_evidence(evidence_id, file_data):
	"""verify a file against its registered hash"""
	evidence = get_evidence(evidence_id)
	
	if evidence is None:
		raise ValueError("Evidence ID not found")
		
	return verify_integrity(file_data, evidence["sha256"])
