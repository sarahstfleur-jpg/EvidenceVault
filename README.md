# EvidenceVault

A digital forensics prototype designed to register digital evidence, verify file integrity, and generate evidence reports using SHA-256 cryptographic hashing.

## Overview

EvidenceVault explores the role of cryptographic hashing in digital forensic investigations. The application provides a user-friendly interface for registering files, recording their digital fingerprints, and detecting subsequent modifications.

## Features

- SHA-256 cryptographic hash generation
- File metadata extraction
- Unique evidence identification using UUIDs
- UTC registration timestamps
- Persistent JSON evidence registry
- File integrity verification
- Downloadable JSON evidence reports
- Interactive Streamlit interface

## Technologies

- Python
- Streamlit
- hashlib
- JSON
- UUID
- Git

## Installation

```bash
git clone https://github.com/sarahstfleur-jpg/EvidenceVault
cd EvidenceVault
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

- `app.py`: Streamlit user interface
- `evidence.py`: Core evidence processing and verification logic
- `registry.json`: Local evidence metadata storage, generated at runtime
- `test_evidence.py`: Functional testing
- `requirements.txt`: Project dependencies

## Design Decisions

The application separates the presentation layer from the core evidence processing logic to reduce coupling, improve maintainability, and support independent testing.

SHA-256 is used to generate cryptographic fingerprints, allowing file contents to be compared against previously registered hashes. UUIDs prevent evidence records with identical filenames from overwriting one another.

## Testing

The application was tested using synthetic evidence files to validate:

- Hash generation
- Evidence registration and retrieval
- Successful verification of unchanged files
- Detection of modified file contents

## Limitations and Future Improvements

EvidenceVault is an educational prototype and is not intended for operational forensic investigations.

Future improvements include:

- Tamper-resistant audit logging
- User authentication and role-based access control
- SQLite database integration
- Chain-of-custody tracking
- PDF report generation

The current implementation verifies file contents against recorded hashes but does not independently establish evidence authenticity or a complete chain of custody.

## Author

Sarah St-Fleur

Carleton University | Cybersecurity (Honours), Minor in Statistics
