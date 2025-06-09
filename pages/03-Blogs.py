import streamlit as st
st.set_page_config(page_title="Blogs", layout="wide")

st.markdown("<p style='text-align: top-right;'>Portfolio</p>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;font-family: serif;'>BLOGS</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("blog1.jpg")
    st.subheader("What is Data Science? A Beginner’s Guide")
    st.write("Data Science is the field of extracting insights and making predictions from data using statistics, programming, and domain knowledge. It involves collecting, cleaning, analyzing, and modeling data to solve real-world problems.")
    st.markdown("[Read Blog](https://medium.com/@shubhambisht149/what-is-data-science-a-beginners-guide-d66aefeb5905)", unsafe_allow_html=True)

# with col2:
#     st.image("https://yourblog.com/img2.jpg")
#     st.subheader("Blog Title 2")
#     st.write("Summary of blog 2...")
#     st.markdown("[Read Blog 2](https://yourblog.com/blog2)", unsafe_allow_html=True)