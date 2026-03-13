import streamlit as st
from components.ai_generate_response import get_blog_outline
from database import save_blog

def ensure_session_state():
    defaults = {
        "topic": "", "seo_keywords": "", "target_audience": None,
        "tone": None, "blog_length": None, "ai_result": None,
        "submitted": False, "loading": False, "current_title": "", 
        "current_content": "", "form_id": 0
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def clear_text_input():
    st.session_state.topic = ""
    st.session_state.seo_keywords = ""
    st.session_state.target_audience = None
    st.session_state.tone = None
    st.session_state.blog_length = None
    st.session_state.ai_result = None
    st.session_state.submitted = False
    st.session_state.loading = False
    st.session_state.current_title = ""
    st.session_state.current_content = ""
    st.session_state.form_id += 1

def handle_regeneration():
    with st.spinner("AI is regenerating..."):
        new_result = get_blog_outline(
            st.session_state.topic, st.session_state.target_audience,
            st.session_state.seo_keywords, st.session_state.tone, st.session_state.blog_length
        )
        st.session_state.ai_result = new_result
        st.session_state.current_title = new_result["title"]
        st.session_state.current_content = new_result["content"]

def reset_for_new_outline():
    st.session_state.submitted = False
    st.session_state.loading = False
    st.session_state.ai_result = None
    st.session_state.current_title = ""
    st.session_state.current_content = ""

def generate_outline():
    ensure_session_state()
    
    if not st.session_state.submitted and not st.session_state.loading:
        with st.form(key=f"input_form_{st.session_state.form_id}", border=False):
            txt = st.text_input("Topic", value=st.session_state.topic)
            
            audience_types = ['Beginners', 'Marketers', 'Developers', 'Others']
            audience = st.radio("Target Audience", audience_types, 
                         index=audience_types.index(st.session_state.target_audience) if st.session_state.target_audience else None, 
                         horizontal=True)
            
            seo = st.text_input("SEO Keywords", value=st.session_state.seo_keywords)
            
            tone_options = ['Friendly', 'Professional', 'Casual', 'Engaging', 'Formal']
            tone = st.radio("Tone", tone_options, 
                          index=tone_options.index(st.session_state.tone) if st.session_state.tone else None, 
                          horizontal=True)
            
            length_options = ['Short (800)', 'Medium (1200)', 'Long (2000)']
            length = st.radio("Length", length_options, 
                         index=length_options.index(st.session_state.blog_length) if st.session_state.blog_length else None, 
                         horizontal=True)

            col0, col1, col2 = st.columns([2, 1, 1])
            with col1:
                st.form_submit_button("Clear", width="stretch", on_click=clear_text_input)
            with col2:
                if st.form_submit_button("Generate Outline", width="stretch"):
                    if all([txt, audience, seo, tone, length]):
                        st.session_state.topic = txt
                        st.session_state.target_audience = audience
                        st.session_state.seo_keywords = seo
                        st.session_state.tone = tone
                        st.session_state.blog_length = length
                        st.session_state.loading = True
                        st.rerun()
                    else:
                        st.warning("Please fill all fields.")

    elif st.session_state.loading:
        with st.spinner("AI is generating..."):
            result = get_blog_outline(
                st.session_state.topic, st.session_state.target_audience,
                st.session_state.seo_keywords, st.session_state.tone, st.session_state.blog_length
            )
            st.session_state.ai_result = result
            st.session_state.current_title = result["title"]
            st.session_state.current_content = result["content"]
            st.session_state.submitted = True
            st.session_state.loading = False
            st.rerun()

    elif st.session_state.submitted:
        with st.form("edit_form", border=False):
            st.session_state.current_title = st.text_input("Title", value=st.session_state.current_title)
            st.session_state.current_content = st.text_area("Content", value=st.session_state.current_content, height=500)

            _c0, c1, c2, c3 = st.columns([2, 1, 1, 1])
            with c1:
                st.form_submit_button("Back", width="stretch", on_click=reset_for_new_outline)
            with c2:
                st.form_submit_button("Regenerate", width="stretch", on_click=handle_regeneration)
            with c3:
                if st.form_submit_button("Save", width="stretch"):
                    save_blog(st.session_state.current_title, st.session_state.current_content)
                    st.switch_page("pages/saved_blogs.py")
