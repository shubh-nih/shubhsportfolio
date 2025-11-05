import streamlit as st

st.markdown("<p style='text-align: top-right;'>Portfolio</p>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;font-family: serif;'>PROJECTS</h1>", unsafe_allow_html=True)

st.sidebar.markdown("# Projects")

st.markdown("## 🤖 Machine Learning Projects")

st.markdown('---')
col1, col2 = st.columns(2, gap = 'large')
with col1:
    st.image('img/gurgaon.png')
    st.markdown('#### Gurgaon Real Estate Capstone Project')
    st.write('''
        A comprehensive data driven solution designed to help users understand, analyze, and make informed property decisions in the Gurgaon housing market.
    ''')
    st.link_button('Live Website', 'https://gurgaon-estate-mlnihs.streamlit.app/')
    st.link_button('GitHub Repo', 'https://github.com/shubh-nih/Gurgaon-RealEstate-ML-Project')
        
with col2:
    st.image('img/tweets.png')
    st.markdown('#### Tweet Sentiment Analysis')
    st.write('''
        A machine learning project that classifies tweets as Positive, or Negative using NLP and Logistic Regression. Built and deployed with Streamlit.
    ''')
    st.link_button('Live Website', 'https://sentiment-analysisnih.streamlit.app/')
    st.link_button('GitHub Repo', 'https://github.com/shubh-nih/Tweets-Sentiment-Analysis')
    

st.markdown("## 📊 Data Analysis Projects")

st.markdown('---')
col1, col2 = st.columns(2, gap = 'large')
with col1:
    st.image('img/indicator.png')
    st.markdown('#### World Indicators Analysis')
    st.write('''
        An end to end data analysis and visualization project leveraging the World Bank API to explore global trends across economy, health, environment, technology, and labor indicators.
    ''')
    st.link_button('GitHub Repo', 'https://github.com/shubh-nih/World-Indicators-Analysis')
        
with col2:
    st.image('img/superstore.png')
    st.markdown('#### Superstore Sales Analysis')
    st.write('''
        An end to end data analysis project exploring sales performance, customer behavior, and regional trends for a retail superstore dataset from Kaggle.
    ''')

    st.link_button('GitHub Repo', 'https://github.com/shubh-nih/Superstore-Sales-Analysis')
    

