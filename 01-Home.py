import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import base64

st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
            
    .profile-pic {
        width: 220px;
        height: 240px;
        border-radius: 60%;
        object-fit: cover;
        border: 5px solid white;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    }
    
    .section-header {
        font-size: 1.8em;
        font-weight: 700;
        margin: 30px 0 20px 0;
        color: #667eea;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
    }
    
    .tech-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 25px;
        border-radius: 10px;
        margin: 15px 0;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .tech-card:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.2);
    }
    
    .tech-card h3 {
        color: #667eea;
        margin-bottom: 12px;
        font-size: 1.2em;
    }
    
    .tech-card ul {
        list-style: none;
        padding-left: 0;
    }
    
    .tech-card li {
        margin: 8px 0;
        color: #333;
        font-weight: 500;
    }
    
    .tech-card li:before {
        content: "▸ ";
        color: #667eea;
        font-weight: bold;
        margin-right: 8px;
    }
    
    hr {
        margin: 40px 0;
        border: 0;
        height: 1px;
        background: linear-gradient(to right, transparent, #667eea, transparent);
    }
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2], gap="large")

with col1:

    profile_pic = Image.open("img/profile.jpg")
    buffer = BytesIO()
    profile_pic.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
        
    st.markdown(f"""
        <div style="display: flex; justify-content: center; padding: 20px 0;">
            <img class="profile-pic" src="data:image/png;base64,{img_base64}">
        </div>
        """, unsafe_allow_html=True)
    
with col2:
    st.markdown("<h1 style='text-align: left;font-family: serif;font-size: 60px;'>SHUBHAM BISHT</h1>", unsafe_allow_html=True)
    st.write("##### Data Science Enthusiast")
    st.write(
         """
         I love transforming raw data into compelling stories and actionable insights. My goal is to leverage technology to solve real world problems efficiently and creatively.
         """
    )
    st.write(
         """
         🔗 **Connect with me:** [Email](mailto:shubhambisht149@gmail.com) | 
         [LinkedIn](https://www.linkedin.com/in/shubhambisht7/) | 
         [GitHub](https://github.com/shubh-nih)
         """
    )

st.markdown("<hr>", unsafe_allow_html=True)

# About Section
st.markdown('<div class="section-header">👨‍💻 About Me</div>', unsafe_allow_html=True)
st.markdown("""
**🎓 Education:** BCA (Bachelor of Computer Applications) from IGNOU, Delhi | Graduating 2027

I'm passionate about uncovering hidden patterns in complex datasets and building predictive models that drive real world impact. 
I specialize in data manipulation, visualization, and machine learning with a focus on writing clean, efficient Python code.

**🎯 What I Do:**
- 📈 Analyze large datasets to identify trends and anomalies
- 🎨 Create compelling visualizations that tell data stories
- 🤖 Build and optimize machine learning models
- 💻 Write production ready Python code

**🏀 Beyond Coding:** Passionate sports enthusiast - Volleyball, Football, Basketball
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Tech Stack Section
st.markdown('<div class="section-header">🛠️ My Tech Stack</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="tech-card">
        <h3>🐍 Languages</h3>
        <ul>
            <li><strong>Python</strong> - Core language for all projects</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tech-card">
        <h3>📊 Data Science Stack</h3>
        <ul>
            <li><strong>Pandas</strong> & <strong>NumPy</strong> - Data manipulation</li>
            <li><strong>Matplotlib</strong>, <strong>Seaborn</strong>, <strong>Plotly</strong> - Visualization</li>
            <li><strong>Scikit-learn</strong> - Machine Learning</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="tech-card">
        <h3>📈 BI & Analytics</h3>
        <ul>
            <li><strong>Power BI</strong> - Business Intelligence</li>
            <li><strong>Tableau</strong> - Data Visualization</li>
            <li><strong>Streamlit</strong> - Web Apps</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div style="text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%); border-radius: 10px; border-left: 5px solid #667eea;">
    <h3 style="color: #667eea; margin-bottom: 10px;">🚀 Ready to Explore?</h3>
    <p>Check out my projects in the <strong>sidebar navigation</strong> to see my work in action!</p>
</div>
""", unsafe_allow_html=True)