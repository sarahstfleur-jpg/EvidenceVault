import streamlit as st
import json

from evidence import (
    register_evidence,
    load_registry,
    verify_evidence,
    calculate_hash
)

st.set_page_config(
    page_title="EvidenceVault",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 EvidenceVault")
st.caption("Digital Evidence Integrity & Verification Tool")

st.divider()

register_tab, verify_tab, registry_tab = st.tabs([
    "Register Evidence",
    "Verify Integrity",
    "Evidence Registry"
])


# TAB 1: REGISTER EVIDENCE

with register_tab:
    st.header("Register Digital Evidence")

    st.write(
        "Upload a file to generate its SHA-256 fingerprint "
        "and create an evidence record."
    )

    uploaded_file = st.file_uploader(
        "Select an evidence file",
        key="register_file"
    )

    if uploaded_file is not None:
        file_data = uploaded_file.getvalue()

        st.write("Filename:", uploaded_file.name)
        st.write("Size:", len(file_data), "bytes")

        if st.button("Register Evidence"):
            record = register_evidence(
                uploaded_file.name,
                file_data
            )

            st.success("Evidence registered successfully!")

            st.write("Evidence ID:")
            st.code(record["evidence_id"])

            st.write("SHA-256 fingerprint:")
            st.code(record["sha256"])

            st.json(record)


# TAB 2: VERIFY INTEGRITY

with verify_tab:
    st.header("Verify Evidence Integrity")

    registry = load_registry()

    if not registry:
        st.info("No evidence has been registered yet.")

    else:
        evidence_id = st.selectbox(
            "Select registered evidence",
            options=list(registry.keys()),
            format_func=lambda eid: (
                f"{registry[eid]['filename']} | {eid}"
            )
        )

        original_record = registry[evidence_id]

        verification_file = st.file_uploader(
            "Upload the file to verify",
            key="verify_file"
        )

        if verification_file is not None:
            if st.button("Verify Integrity"):
                file_data = verification_file.getvalue()

                result = verify_evidence(
                    evidence_id,
                    file_data
                )

                st.write("Original SHA-256:")
                st.code(original_record["sha256"])

                st.write("Current SHA-256:")
                st.code(calculate_hash(file_data))

                if result:
                    st.success(
                        "Integrity verified. "
                        "The file matches the registered hash."
                    )
                else:
                    st.error(
                        "Integrity check failed. "
                        "The file contents do not match "
                        "the registered hash."
                    )


# TAB 3: EVIDENCE REGISTRY

with registry_tab:
    st.header("Evidence Registry")

    registry = load_registry()

    st.metric("Registered Evidence", len(registry))

    if not registry:
        st.info("The evidence registry is empty.")

    else:
        st.dataframe(
            list(registry.values()),
            use_container_width=True,
            hide_index=True
        )

        selected_id = st.selectbox(
            "Select evidence to export",
            options=list(registry.keys()),
            format_func=lambda eid: (
                f"{registry[eid]['filename']} | {eid}"
            ),
            key="export_evidence"
        )

        report = json.dumps(
            registry[selected_id],
            indent=4
        )

        st.download_button(
            label="Download Evidence Report",
            data=report,
            file_name=f"report_{selected_id}.json",
            mime="application/json"
        )


st.divider()

st.caption(
    "EvidenceVault | Digital Forensics Prototype | "
    "SHA-256 Integrity Verification"
)
