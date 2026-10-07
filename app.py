import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="MEHMOOD UL HASSAN SHAH | Portfolio", layout="wide")

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Read HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Encode Profile 2.jpeg into base64 string
img_base64 = get_base64_image("Profile 2.jpeg")

if img_base64:
    base64_src = f"data:image/jpeg;base64,{img_base64}"
    # Replace any profile image source with base64 data
    html_content = html_content.replace("Profile 2.jpeg", base64_src)
    html_content = html_content.replace("https://raw.githubusercontent.com/shah31300/my-portfolio/main/Profile%202.jpeg", base64_src)

# Render full height HTML
components.html(html_content, height=2200, scrolling=True)