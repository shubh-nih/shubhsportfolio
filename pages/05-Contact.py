import streamlit as st
st.set_page_config(page_title="Contacts", layout="wide")

st.markdown("<p style='text-align: top-right;'>Portfolio</p>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;font-family: serif;'>CONTACT INFO</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("[📧 Email](mailto:shubhambisht149@gmail.com)")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/shubhambisht7/)")
with col2:
    st.markdown("[🐙 GitHub](https://github.com/shubh-nih)")
    st.markdown("[📊 Kaggle](https://www.kaggle.com/nihshu)")


