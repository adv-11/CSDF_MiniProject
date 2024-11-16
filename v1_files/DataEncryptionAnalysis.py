from cryptography.fernet import Fernet
import hashlib

# Generate a secret key for encryption
def generate_key():
    return Fernet.generate_key()


# Encrypt data
def encrypt_data(key, plaintext):
    cipher_suite = Fernet(secret_key)
    encrypted_text = cipher_suite.encrypt(plaintext.encode())
    return encrypted_text


# Decrypt data
def decrypt_data(key, encrypted_text):
    cipher_suite = Fernet(secret_key)
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text


# Function to compute the SHA-256 hash of data
def calculate_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    return sha256.digest()


# Function to verify data integrity
def verify_integrity(original_data, decrypted_data):
    original_hash = calculate_hash(original_data)
    decrypted_hash = calculate_hash(decrypted_data)

    return original_hash == decrypted_hash

# Function to verify data confidentiality
def check_confidentiality(encrypted_string, encryption_key):
    try:
        cipher_suite = Fernet(encryption_key)
        decrypted_data = cipher_suite.decrypt(encrypted_string)
        print("Data is confidential. Decryption successful.")
    except Exception as e:
        print("Data is confidential. Decryption failed.")

# Function to verify data availability
def check_availability(encrypted_string, encryption_key):
    try:
        cipher_suite = Fernet(encryption_key)
        decrypted_data = cipher_suite.decrypt(encrypted_string)
        print("Data is available. Decryption successful.")
    except Exception as e:
        print("Data is not available. Decryption failed.")


if __name__ == "__main__":

    # Generate a secret key
    print("Secrete Key Generated ... ")
    secret_key = generate_key()
    #print(secret_key)

    # Data to be encrypted
    data_to_encrypt = "This is a top level secret"

    # Encrypt the data
    encrypted_data = encrypt_data(secret_key, data_to_encrypt)
    print("Encrypted data:", encrypted_data)

    # Decrypt the data
    decrypted_data = decrypt_data(secret_key, encrypted_data)
    print("Decrypted data:", decrypted_data)
    
    # To verify data integrity
    if verify_integrity(data_to_encrypt, decrypted_data):
        print("Data integrity is intact.")
    else:
        print("Data integrity check failed. The data may have been tampered with.")
    
    # To verify data confidentiality    
    check_confidentiality(encrypted_data, secret_key)
    
    # To verify data availability
    check_availability(encrypted_data, secret_key)
