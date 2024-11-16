import os
import hashlib
import logging

# Define a list of sensitive file and directory names
SENSITIVE_ENTRIES = ["sample.log"]

# Define the list of files and directories to check for availability
availability = ['CyberForensics.py', 'DataEncryptionAnalysis.py', 'FileAnalysis.py','adv.txt','log.py','LogAnalysis.py', 'sample.log']

# Configure logging
logging.basicConfig(filename='file_analysis.log', level=logging.ERROR)

def calculate_checksum(file_path):
    # Calculate MD5 checksum of a file
    md5 = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                md5.update(chunk)
        return md5.hexdigest()
    except Exception as e:
        logging.error(f"Error calculating checksum for {file_path}: {str(e)}")
        return None

def analyze_file_system(directory):
    try:
        # Validate and sanitize user input for directory
        directory = os.path.abspath(directory)
        
        # Check if the directory exists and is a valid directory
        if not os.path.exists(directory) or not os.path.isdir(directory):
            print(f"Directory '{directory}' not found or is not a valid directory.")
            return

        # Check if the script has permission to access the directory
        if not os.access(directory, os.R_OK):
            print(f"Permission denied to access directory '{directory}'.")
            return

        # Create a dictionary to store checksums
        checksums = {}

        # List files and directories in the specified directory
        entries = os.listdir(directory)
        print("-->",entries)

        # Check the availability of specified items
        for item in availability:
            print(item)
            if item not in entries:
                logging.error(f"'{item}' is not available in the target directory.")

        # Analyze each entry (file or directory)
        for entry in entries:
            entry_path = os.path.join(directory, entry)
            entry_type = "File"
            
            if os.path.isdir(entry_path):
                entry_type = "Directory"
            else:
                # Calculate and store the checksum for files
                checksum = calculate_checksum(entry_path)
                if checksum is not None:
                    checksums[entry] = checksum
            
            # Exclude sensitive entries from printing and logging
            if entry in SENSITIVE_ENTRIES:
                continue
            
            # Extract basic metadata
            entry_size = os.path.getsize(entry_path)
            entry_creation_time = os.path.getctime(entry_path)
            entry_modification_time = os.path.getmtime(entry_path)
            
            # Print metadata (You can choose to log this securely instead of printing)
            print(f"Entry Type: {entry_type}")
            print(f"Entry Name: {entry}")
            print(f"Size: {entry_size} bytes")
            print(f"Creation Time: {entry_creation_time}")
            print(f"Modification Time: {entry_modification_time}")
            print()

        # Check integrity by comparing checksums
        print("Integrity Check:")
        for entry, checksum in checksums.items():
            print(f"{entry}: {checksum}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    target_directory = r"C:\Users\Advait Shinde\CSDF_MiniProject" 
    analyze_file_system(target_directory)


