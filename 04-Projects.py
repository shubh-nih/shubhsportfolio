import streamlit as st

st.markdown("<p style='text-align: top-right;'>Portfolio</p>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;font-family: serif;'>PROJECTS</h1>", unsafe_allow_html=True)

st.sidebar.markdown("# Projects")

col1, col2 = st.columns(2)
with col1:
    st.image('img/gurgaon.png')
    st.markdown('#### Gurgaon RealEstate ML Capstone Project')
    st.write('''
        A comprehensive data driven solution designed to help users understand, analyze, and make informed property decisions in the Gurgaon housing market.
    ''')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button('Live Website', 'https://gurgaon-estate-mlnihs.streamlit.app/')
    with col2:
        st.link_button('GitHub Repo', 'https://github.com/shubh-nih/Gurgaon-RealEstate-ML-Project')