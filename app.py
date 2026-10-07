import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="MEHMOOD UL HASSAN SHAH | Portfolio", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit default padding and headers
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem;}
    </style>
""", unsafe_allow_html=True)

def load_base64_image(image_filename):
    # Search in current directory
    possible_paths = [
        image_filename,
        "Profile 2.jpeg",
        "profile 2.jpeg",
        "Profile 2.jpg",
        "Profile_2.jpeg"
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            with open(path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
    return None

# Read HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Get Base64 image string
img_b64 = load_base64_image("Profile 2.jpeg")

if img_b64:
    b64_url = f"data:image/jpeg;base64,{img_b64}"
    # Replace all profile src attributes regardless of how they are written in index.html
    import re
    html_content = re.sub(r'src=["\'][^"\']*Profile[^"\']*["\']', f'src="{b64_url}"', html_content)
    html_content = re.sub(r'src=["\']Profile 2\.jpeg["\']', f'src="{b64_url}"', html_content)

# Render full height HTML
components.html(html_content, height=2200, scrolling=True)