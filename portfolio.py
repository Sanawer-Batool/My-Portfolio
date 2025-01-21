import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image, ImageDraw

st.set_page_config(page_title="Sanawer's Portfolio", page_icon=":house_with_garden:", layout="wide")


html_code = """
<div style="text-align: center;">
    <h1 style="font-size: 3em; animation: fadeIn 3s ease-in-out;">
        Welcome to My Portfolio!
    </h1>
</div>

<style>
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
h1 {
    color: purple;
}
</style>
"""
st.markdown(html_code, unsafe_allow_html=True)

st.write("##")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_UBiAADPga8.json")
lottie_contact = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_lt8ter7g.json")

image1 = Image.open("images/Lily.jfif")
image2 = Image.open("images/sales.jfif")
image3 = Image.open("images/excel.jfif")
image4 = Image.open("images/video.jfif")
uploaded_image_path = "images/dp.jfif" 
dp = Image.open(uploaded_image_path).convert("RGBA")

dp = dp.resize((170, 170)) 


mask = Image.new("L", dp.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, dp.size[0], dp.size[1]), fill=255)

circular_dp = Image.new("RGBA", dp.size)
circular_dp.paste(dp, (0, 0), mask)

circular_dp_path = "circular_dp.png"
circular_dp.save(circular_dp_path)

col1, col2 = st.columns([1, 4])  

with col1:
    st.image(circular_dp_path, caption="Data Scientist", use_container_width=False)

with col2:
    st.header("SANAWER BATOOL :cherry_blossom:")
    st.subheader("_Data Scientist | Data Analyst | Data Engineer | AI/ML Enthusiast_")
    st.write("""
    This is My Portfolio, containing my Projects, Skills, and contact info!!! :angel:
    """)
    st.write("[You can build too😸](https://docs.streamlit.io/get-started)")

st.write("---")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects', 'Skills' ,'Contact'],
        icons = ['person', 'code-slash', 'clipboard-data-fill','chat-left-text-fill'],
        orientation = 'horizontal'
    )

if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("#####")
            st.title("ABOUT ME!")
            st.write("Hey! I’m an undergrad at the University of Central Punjab, and I’m really excited about data analysis, data science, machine learning, deep learning, and AI. I love diving into new tech and exploring innovative solutions!")
            st.write("Outside of academics, I enjoy reading books, watching animated movies, and taking walks.")

        with col2:
            st_lottie(lottie_coder)

    st.write("---")
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.markdown("""
            ### 📘 **Education**
            - **University of Central Punjab**
                - **BS Data Science**
                - **CGPA Progression:**
                    - 🏆 **3.9** → 1st Semester
                    - 🏆 **3.87** → 2nd Semester
                    - 🏆 **3.74** → 3rd Semester
                    - 🏆 **3.73** → 4th Semester\n
            - **Punjab Group of Colleges**
                - FSc. Pre-Engineering\n
            - **The Educators School**
                - Matriculation
            """)
        with col4:
            st.markdown("""
            ### 💼 **Experience**
            - **Internship**
                - **Company:** IREG-IT  
                - **Duration:** 6 months\n 
            - **Cold Email Writer**
                - **Company:** Brandify Logics  
            """)

if selected == 'Projects':

    projects = [
        {
            "title": "AI Cancer Cell Detection",
            "image": image1,  
            "file_name": "Cancer_Detect.zip",
            "description": """In this project, I trained an AI model to detect cancer cells using advanced machine learning techniques.""",
            "key_achievement": "The AI model can detect cancer cells with over 97% accuracy.",
            "technologies": "Python, TensorFlow, NumPy, Pandas, Scikit-learn.",
        },
        {
            "title": "Supermarket Sales Analysis",
            "image": image2,  
            "file_name": "pythonProjectUD.zip",
            "description": """In this project, I performed data cleaning, analysis, and visualization on supermarket sales data to uncover key insights.""",
            "key_achievement": "Identified the most sold product, analyzed buyer demographics (e.g., male vs. female and age groups), and evaluated revenue patterns.",
            "technologies": "Python, Pandas, NumPy, Matplotlib, Seaborn.",
        },
        {
            "title": "Excel Dashboard for Data Analysis",
            "image": image3,  
            "file_name": "Excel_DashBoard.zip",
            "description": """In this project, I performed data cleaning, analysis, and visualization directly in Excel to uncover trends and insights.""",
            "key_achievement": "Created an interactive Excel dashboard using pivot tables, pivot charts, and slicers to present data effectively.",
            "technologies": "Microsoft Excel.",
        },
        {
            "title": "Video Editing Social Media Apps",
            "image": image4,  
            "file_name": "Social_Media.mp4",
            "description": """In this project, I did animation of Social Media apps.""",
            "key_achievement": "I added keyframes for animation.",
            "technologies": "Capcut.",
        },
    ]

    if "selected_project" not in st.session_state:
        st.session_state.selected_project = None

    def reset_project():
        st.session_state.selected_project = None

    if st.session_state.selected_project is None:
        st.header("My Projects 👩‍💻")
        st.write("##")

        for project in projects:
            col1, col2 = st.columns((1, 2))
            with col1:
                st.image(project["image"], caption=project["title"], use_container_width=True)
            with col2:
                st.markdown(f"### {project['title']}")
                if st.button(f"Read More about {project['title']}", key=project['title']):
                    st.session_state.selected_project = project
            st.divider()

    else:
        project = st.session_state.selected_project
        st.header(f"{project['title']} Details")
        st.markdown(f"- **Description:** {project['description']}")
        st.markdown(f"- **Key Achievement:** {project['key_achievement']}")
        st.markdown(f"- **Technologies Used:** {project['technologies']}")
        with open(project["file_name"], "rb") as file:
            st.download_button(
                label=f"Download {project['title']}",
                data=file,
                file_name=project["file_name"],
                mime="application/zip" if project["file_name"].endswith(".zip") else "video/mp4",
            )
        if st.button("Back to Projects"):
            reset_project()

  

if selected == 'Contact':
    st.header("Get In Touch!!!")
    st.write("[My Linkedln:smile:](https://www.linkedin.com/in/sanawer-batool-9566a6256/)")

    left_col, right_col = st.columns((1, 2))

    with left_col:
        st.markdown(
            """
            <form action="https://formsubmit.co/sanawerb246@gmail.com" method="POST" style="text-align: left;">
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name" required style="width: 100%; padding: 5px; margin-bottom: 10px;"><br>
                <label for="email">Email:</label><br>
                <input type="email" id="email" name="email" required style="width: 100%; padding: 5px; margin-bottom: 10px;"><br>
                <label for="message">Message:</label><br>
                <textarea id="message" name="message" rows="4" required style="width: 100%; padding: 5px; margin-bottom: 10px;"></textarea><br>
                <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer;">Send</button>
            </form>
            """,
            unsafe_allow_html=True,
        )
    
    with right_col:
        st_lottie(lottie_contact, height= 300)

if selected == 'Skills':
    st.title("Skills")

    skills = """
        <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">
            <div style="text-align: center;">
                <i class="fas fa-cogs" style="font-size: 50px; color: #ff6347;"></i>
                <p>C++</p>
            </div>
            <div style="text-align: center;">
                <i class="fas fa-database" style="font-size: 50px; color: #32cd32;"></i>
                <p>Database</p>
            </div>
            <div style="text-align: center;">
                <i class="fab fa-django" style="font-size: 50px; color: #0e76a8;"></i>
                <p>Django</p>
            </div>
            <div style="text-align: center;">
                <i class="fab fa-python" style="font-size: 50px; color: #306998;"></i>
                <p>Python</p>
            </div>
            <div style="text-align: center;">
                <i class="fas fa-cogs" style="font-size: 50px; color: #8b0000;"></i>
                <p>KNIME</p>
            </div>
            <div style="text-align: center;">
                <i class="fas fa-laptop" style="font-size: 50px; color: #ffd700;"></i>
                <p>MS Office</p>
            </div>
            <div style="text-align: center;">
                <i class="fas fa-video" style="font-size: 50px; color: #ff1493;"></i>
                <p>Video Editing</p>
            </div>
            <div style="text-align: center;">
                <i class="fas fa-search" style="font-size: 50px; color: #00bfff;"></i>
                <p>Beautiful Soup</p>
            </div>
            <div style="text-align: center;">
                <i class="fas fa-search" style="font-size: 50px; color: #00bfff;"></i>
                <p>Scrapy</p>
            </div>
        </div>
    """
    
    st.markdown(skills, unsafe_allow_html=True)


