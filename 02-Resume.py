import streamlit as st
import base64
st.markdown("<p style='text-align: top-right;'>Portfolio</p>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;font-family: serif;'>RESUME</h1>", unsafe_allow_html=True)

st.sidebar.markdown("# Resume")

with open("shubham-ml-resume.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()
    
st.download_button(
    label="📄 Download Resume",
    data=pdf_bytes,
    file_name="shubham-ml-resume.pdf",
    mime="application/pdf"
)

# Display PDF using iframe
st.markdown(
    f'<iframe src="data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode()}" width="700" height="800" type="application/pdf"></iframe>',
    unsafe_allow_html=True
)