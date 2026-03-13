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
st.write("Generate a structured blog outline tailored to your topic and audience using **OpenAI's** language models. Fill in the details below and click **'Generate Outline'** to get started.")
st.markdown("---")

# Invoke the generate_outline function to generate the outline
generate_outline()

