# app.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cognifront Analytics", layout="wide")

with open("dashboard.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1800, scrolling=True)