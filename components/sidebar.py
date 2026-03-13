import streamlit as st

def _render_navigation():
    """Render the navigation bar at the sidebar."""
    st.sidebar.title("AI - Blog Outline Generator")
    with st.sidebar:
        st.markdown("---")
        st.page_link("pages/saved_blogs.py", label="View saved Blogs", icon=":material/bookmarks:")
        st.page_link("main.py", label="Generate New Blog", icon=":material/add:")
