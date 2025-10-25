import streamlit as st
import datetime
import pytz

ist = pytz.timezone('Asia/Kolkata')
now_ist = datetime.datetime.now(ist)

st.markdown("<p style='text-align: top-right;'>Portfolio</p>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;font-family: serif;'>Get In Touch</h1>", unsafe_allow_html=True)

st.sidebar.markdown("# Contacts")


col1, col2 = st.columns([2, 1])    
with col1:
    st.markdown("""
    **Email:**  
    shubhambisht149@gmail.com
    """)

st.markdown("---")

with col2:
    st.markdown("""
    Profile:
    - [LinkedIn](https://www.linkedin.com/in/shubhambisht7/)
    - [GitHub](https://github.com/shubh-nih)
    """)

st.caption(f"""Timezone   
           Current Date & Time: 
           
           {now_ist.strftime('%Y-%m-%d %I:%M %p')} (IST)  
""")