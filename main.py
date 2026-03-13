import streamlit as st
from components.generate_outline import generate_outline
from components.sidebar import _render_navigation

st.set_page_config(page_title="AI - Blog Outline Generator", page_icon="⚡", layout="centered")

states = ["topic", "seo_keywords"]

if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "loading" not in st.session_state:
    st.session_state.loading = False

for state in states:
    if state not in st.session_state:
        st.session_state[state] = ""
    
_render_navigation()
        
st.markdown("## 📝 Blog Outline Generator")
st.write("Welcome to the AI Blog Outline Generator! This tool uses OpenAI's ChatGPT to generate a blog outline based on your topic and target audience. Simply fill in the form and click 'Generate Outline' to get started.")
st.markdown("---")

# Invoke the generate_outline function to generate the outline
generate_outline()

