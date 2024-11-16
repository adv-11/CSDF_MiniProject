import streamlit as st
from cryptography.fernet import Fernet
import hashlib

def generate_key():
    return Fernet.generate_key()

def encrypt_data(key, plaintext):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(plaintext.encode())

def decrypt_data(key, encrypted_text):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_text).decode()

def calculate_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    return sha256.digest()

st.title("Data Encryption")

with st.expander('Click here to view Flowchart '):
    st.image('1.drawio.png')

if "secret_key" not in st.session_state:
    st.session_state.secret_key = generate_key()

data_to_encrypt = st.text_input("Enter data to encrypt:")
if st.button("Encrypt Data"):
    if data_to_encrypt:
        encrypted_data = encrypt_data(st.session_state.secret_key, data_to_encrypt)
        st.write("Encrypted Data:", encrypted_data)

        decrypted_data = decrypt_data(st.session_state.secret_key, encrypted_data)
        st.write("Decrypted Data:", decrypted_data)

        original_hash = calculate_hash(data_to_encrypt)
        decrypted_hash = calculate_hash(decrypted_data)
        integrity_status = "intact" if original_hash == decrypted_hash else "tampered"
        st.write(f"Data integrity is {integrity_status}.")
    else:
        st.error("Please provide data to encrypt.")
