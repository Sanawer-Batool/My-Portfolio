# My-Portfolio

# Documentation for My Portfolio

## Overview

My Portfolio is an interactive web-based application built using Streamlit. The portfolio showcases Sanawer Batool's skills, projects, education, and contact information in a visually engaging manner. The application leverages multimedia content, animations, and a user-friendly layout to provide an immersive experience.

## Key Features

1. **Dynamic Page Layout**: The application is structured with clear sections such as About, Projects, Skills, and Contact, navigable via an intuitive horizontal menu.
2. **Interactive Elements**: Users can interact with the application to explore project details, view animations, and submit contact forms.
3. **Responsive Design**: The portfolio is designed to be visually appealing and functional across different devices and screen sizes.
4. **Media Integration**: The use of Lottie animations, images, and styled text enhances user engagement.

---

## Implementation Details

### 1. **Technology Stack**

- **Framework**: Streamlit
- **Libraries**:
  - `requests`: For fetching Lottie animation files.
  - `streamlit_option_menu`: For creating a navigation menu.
  - `streamlit_lottie`: For integrating Lottie animations.
  - `Pillow`: For image processing.

---

### 2. **Page Setup**

The application uses Streamlit's `set_page_config` to define the page title, icon, and layout.

```python
st.set_page_config(page_title="Sanawer's Portfolio", page_icon=":house_with_garden:", layout="wide")
```

---

### 3. **Sections**

#### a. **Welcome Section**

- **Description**: A welcoming header with a fade-in animation effect.
- **Code Snippet**:

```python
html_code = """
<div style="text-align: center;">
    <h1 style="font-size: 3em; animation: fadeIn 3s ease-in-out;">
        Welcome to My Portfolio!
    </h1>
</div>
"""
st.markdown(html_code, unsafe_allow_html=True)
```

---

#### b. **About Section**

- **Content**:
  - Personal introduction with academic and extracurricular details.
  - Animated Lottie visualization.
- **Key Code Snippet**:

```python
if selected == 'About':
    st.title("ABOUT ME!")
    st.write("Hey! I’m an undergrad at the University of Central Punjab, ...")
    st_lottie(lottie_coder)
```

---

#### c. **Projects Section**

- **Features**:
  - Displayed as a list of projects with title, description, and key achievements.
  - Each project includes a downloadable file and detailed information.
- **Code Snippet**:

```python
projects = [
    {
        "title": "AI Cancer Cell Detection",
        "description": "In this project, I trained an AI model ...",
        "technologies": "Python, TensorFlow, NumPy, Pandas",
    }
]
```

---

#### d. **Skills Section**

- **Content**: Display of technical skills with associated icons.
- **Implementation**:

```python
skills = """
<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">
    <div style="text-align: center;">
        <i class="fab fa-python" style="font-size: 50px; color: #306998;"></i>
        <p>Python</p>
    </div>
</div>
"""
st.markdown(skills, unsafe_allow_html=True)
```

---

#### e. **Contact Section**

- **Features**:
  - Integrated form for name, email, and message.
  - Submissions sent via FormSubmit.
- **Code Snippet**:

```python
st.markdown(
    """
    <form action="https://formsubmit.co/sanawerb246@gmail.com" method="POST">
        <input type="text" name="name" required>
        <input type="email" name="email" required>
        <textarea name="message" rows="4" required></textarea>
    </form>
    """,
    unsafe_allow_html=True,
)
```

---

### 4. **Media Processing**

- **Circular Profile Image**:
  - Created using `Pillow` to generate a circular mask and apply it to the profile picture.
  - **Code Snippet**:
  ```python
  dp = Image.open("dp.jfif").convert("RGBA")
  mask = Image.new("L", dp.size, 0)
  draw = ImageDraw.Draw(mask)
  draw.ellipse((0, 0, dp.size[0], dp.size[1]), fill=255)
  circular_dp.paste(dp, (0, 0), mask)
  ```

---

### 5. **Lottie Animations**

- Lottie animations are fetched dynamically using the `requests` library.
- **Key Code Snippet**:

```python
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coder = load_lottieurl("https://assets5.lottiefiles.com/...json")
```


