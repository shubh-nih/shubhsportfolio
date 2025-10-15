import streamlit as st
st.set_page_config(layout = 'wide')

home = st.Page("01-Home.py", title="Home", icon="🏠")
resume = st.Page("02-Resume.py", title="Resume", icon="📄")
blogs = st.Page("03-Blogs.py", title="Blogs", icon="✍️")
projects = st.Page("04-Projects.py", title="Projects", icon="💼")
contact = st.Page("05-Contact.py", title="Contact", icon="📞")

# Set up navigation
pg = st.navigation([home, resume, blogs, projects, contact])

# Run the selected page
pg.run()