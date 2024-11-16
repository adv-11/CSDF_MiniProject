import os
import hashlib
import logging
import streamlit as st

# Define a list of sensitive file and directory names
SENSITIVE_ENTRIES = ["sample.log"]

# Define the list of files and directories to check for availability
availability = ['CyberForensics.py', 'data_encryption.py', 'file_analysis.py', 'log.py', 'log_analysis.py', 'sample.log', 'app.py']


# Baseline checksums for integrity verification
baseline_checksums = {
    'sample.log': '91723c0205d66f4f8e9d346433594337'
}

# Configure logging
logging.basicConfig(filename='file_analysis.log', level=logging.ERROR)

def calculate_checksum(file_path):
    """Calculate the MD5 checksum of a file."""
    md5 = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                md5.update(chunk)
        file_checksum = md5.hexdigest()
        
        # Compare with the baseline checksum
        file_name = os.path.basename(file_path)
        if file_name in baseline_checksums and baseline_checksums[file_name] != file_checksum:
            logging.error(f"Integrity check failed for {file_name}. Expected {baseline_checksums[file_name]}, got {file_checksum}")
        return file_checksum
    except Exception as e:
        logging.error(f"Error calculating checksum for {file_path}: {str(e)}")
        return None

def analyze_file_system(directory):
    """Analyze the file system for availability and checksum integrity."""
    results = {"availability": [], "file_metadata": [], "checksums": {}}
    try:
        # Validate and sanitize user input for directory
        directory = os.path.abspath(directory)
        
        # Check if the directory exists and is a valid directory
        if not os.path.exists(directory) or not os.path.isdir(directory):
            st.error(f"Directory '{directory}' not found or is not a valid directory.")
            logging.error(f"Directory '{directory}' not found or is not a valid directory.")
            return results

        # Check if the script has permission to access the directory
        if not os.access(directory, os.R_OK):
            st.error(f"Permission denied to access directory '{directory}'.")
            return results

        # List files and directories in the specified directory
        entries = os.listdir(directory)
        results["availability"] = [item for item in availability if item in entries]

        # Analyze each entry (file or directory)
        for entry in entries:
            entry_path = os.path.join(directory, entry)
            entry_type = "File" if os.path.isfile(entry_path) else "Directory"
            
            # Calculate and store the checksum for files
            if entry_type == "File":
                checksum = calculate_checksum(entry_path)
                if checksum is not None:
                    results["checksums"][entry] = checksum

            # Skip sensitive entries in the results
            if entry in SENSITIVE_ENTRIES:
                continue
            
            # Extract metadata
            entry_metadata = {
                "Type": entry_type,
                "Name": entry,
                "Size (bytes)": os.path.getsize(entry_path),
                "Creation Time": os.path.getctime(entry_path),
                "Modification Time": os.path.getmtime(entry_path),
                "Checksum": checksum
            }
            results["file_metadata"].append(entry_metadata)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        st.error(f"An error occurred: {str(e)}")

    return results

# Streamlit UI
st.title("File System Integrity Analyzer")

directory = st.text_input("Enter Directory Path:")

if st.button("Analyze Directory"):
    if directory:
        analysis_results = analyze_file_system(directory)
        
        # Display availability of files
        st.subheader("Availability Check")
        if analysis_results["availability"]:
            st.write("The following files are available in the directory:")
            for item in analysis_results["availability"]:
                st.write(f"- {item}")
        else:
            st.write("No specified files are available in the directory.")

        # Display file metadata
        st.subheader("File Metadata")
        for metadata in analysis_results["file_metadata"]:
            st.write(metadata)

        # Display checksum results
        st.subheader("Integrity Check (Checksums)")
        for entry, checksum in analysis_results["checksums"].items():
            st.write(f"{entry}: {checksum}")
            # Display an error if the checksum does not match the baseline
            if entry in baseline_checksums and baseline_checksums[entry] != checksum:
                st.error(f"Integrity check failed for {entry}. Expected {baseline_checksums[entry]}, got {checksum}")
            else:
                st.success(f"Integrity check passed for {entry}.")

    else:
        st.error("Please enter a valid directory path.")
