import streamlit as st
import streamlit.components.v1 as components

# Set full browser width and page title
st.set_page_config(page_title="MEHMOOD UL HASSAN SHAH | Portfolio", layout="wide")

# Read and render index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render HTML inside Streamlit iframe
components.html(html_content, height=2000, scrolling=True)