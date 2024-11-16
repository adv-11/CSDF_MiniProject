import streamlit as st

st.set_page_config(page_title="Cybersecurity Forensics App", layout="wide")

# Sidebar navigation
st.sidebar.title("Cybersecurity Forensics")

with st.sidebar.expander('Group ID : A3'):
    st.write('Sakshi Ingale - 41021')
    st.write('Yash Jangale - 41028')
    st.write('Gayatri Kurulkar - 41039')
    st.write('Advait Shinde - 41058')
    
page = st.sidebar.selectbox("Select Analysis", ["Home", "File Analysis", "Data Encryption", "Log Analysis"])

# Navigation logic
if page == "Home":
    st.title("Cybersecurity Forensics Dashboard")
    st.write("Select an option from the sidebar to begin.")
elif page == "File Analysis":
    exec(open("pages/file_analysis.py").read())
elif page == "Data Encryption":
    exec(open("pages/data_encryption.py").read())
elif page == "Log Analysis":
    exec(open("pages/log_analysis.py").read())
