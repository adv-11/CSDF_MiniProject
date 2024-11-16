import hashlib
import collections
import re

# Function to calculate a checksum/hash of the log file
def calculate_checksum(log_file_path):
    try:
        with open(log_file_path, 'r') as log_file:
            content = log_file.read()
            checksum = hashlib.sha256(content.encode()).hexdigest()
            return checksum
    except FileNotFoundError:
        return None

# Function to mask sensitive information in log entries
def mask_sensitive_info(log_entry):
    # Customize this function to mask sensitive information based on your log format
    # For example, you can mask passwords or IP addresses.
    log_entry = re.sub(r'password=\S+', 'password=***MASKED***', log_entry, flags=re.IGNORECASE)
    log_entry = re.sub(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', '***MASKED IP***', log_entry)
    return log_entry

# Function to check the integrity of the log file and retrieve its content
def check_log_file(log_file_path):
    try:
        with open(log_file_path, 'r') as log_file:
            log_content = log_file.read()
            return log_content, calculate_checksum(log_file_path)
    except FileNotFoundError:
        return None, None

def analyze_logs(log_file_path):
    try:
        # Check the availability of the log file and retrieve its content and checksum
        log_content, original_checksum = check_log_file(log_file_path)
        # print(log_content, original_checksum)
        
        if log_content is None:
            print(f"Log file not found: {log_file_path}")
            print("Log file is not available.")
            return
        else: 
            print("Logs are available")
        
        # Check the integrity of the log file
        if original_checksum is None:
            print("Log file checksum not found. Integrity check skipped.")
        else:
            current_checksum = hashlib.sha256(log_content.encode()).hexdigest()
            if current_checksum != original_checksum:
                print("Log file integrity: Modified")
                return
        
        log_entry_counts = collections.Counter()
        
        for line in log_content.splitlines():
            log_entry_match = re.match(r'\[(.*?)\] (\S+) (.+)', line)
            if log_entry_match:
                timestamp, username, event_description = log_entry_match.groups()
                
                # Mask sensitive information in the log entry
                masked_log_entry = mask_sensitive_info(line)
                
                if "login failed" in event_description.lower():
                    log_entry_counts[masked_log_entry] += 1
        print("Logs are confidential")
        
        most_common_entries = log_entry_counts.most_common(10)
        print("Most common log entries:")
        for entry, count in most_common_entries:
            print(f"{entry}: {count} occurrences")
        
        print("Log file integrity: OK")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    log_file_path = "sample.log"  
    analyze_logs(log_file_path)
