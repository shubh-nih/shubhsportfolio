import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
st.markdown("<p style='text-align: top-right;'>Portfolio</p>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;font-family: serif;'>RESUME</h1>", unsafe_allow_html=True)

st.sidebar.markdown("# Resume")

# Display PDF
pdf_viewer("shubham-ml-resume.pdf", width=700)

# Add download button
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    with open("shubham-ml-resume.pdf", "rb") as pdf_file:
        st.download_button(
            label="⬇️ Download Resume",
            data=pdf_file,
            file_name="shubham-ml-resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )