import streamlit as st
import hashlib
import re
import collections

def calculate_checksum(log_content):
    return hashlib.sha256(log_content.encode()).hexdigest()

def mask_sensitive_info(log_entry):
    log_entry = re.sub(r'password=\S+', 'password=***MASKED***', log_entry, flags=re.IGNORECASE)
    log_entry = re.sub(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', '***MASKED IP***', log_entry)
    return log_entry

st.title("Log Analysis")

uploaded_file = st.file_uploader("Choose a log file")
if uploaded_file is not None:
    log_content = uploaded_file.read().decode("utf-8")
    original_checksum = calculate_checksum(log_content)

    st.subheader("Log Content (Masked)")
    masked_content = "\n".join([mask_sensitive_info(line) for line in log_content.splitlines()])
    st.text_area("Masked Log Content", masked_content, height=300)

    st.subheader("Log Integrity Check")
    current_checksum = calculate_checksum(log_content)
    integrity_status = "OK" if current_checksum == original_checksum else "Modified"
    st.write(f"Log file integrity: {integrity_status}")
    
    log_entry_counts = collections.Counter(masked_content.splitlines())
    st.subheader("Most Common Entries")
    st.write(log_entry_counts.most_common(10))
