import streamlit as st

st.set_page_config(page_title="Student Safety Reporting", layout="centered")

st.title("🛡️ Student Safety Reporting")
st.write("Please submit any safety concerns anonymously below.")

message = st.text_area("Your safety concern:")

if st.button("Submit"):
    if message.strip():
        st.success("✅ Thank you! Your report has been received.")
    else:
        st.warning("⚠️ Please write something before submitting.")
