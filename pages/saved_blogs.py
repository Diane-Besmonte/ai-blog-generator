import streamlit as st
from components.sidebar import _render_navigation
from database import get_saved_blogs, get_blog_by_id

_render_navigation()

st.markdown("## 💾 Saved Blogs")
st.markdown("##### View and manage your AI-generated blog outlines and content.")
st.markdown("---")

if "selected_blog_id" not in st.session_state:
    st.session_state.selected_blog_id = None

if st.session_state.selected_blog_id:
    blog = get_blog_by_id(st.session_state.selected_blog_id)
    
    if st.button("← Back to List"):
        st.session_state.selected_blog_id = None
        st.rerun()
        
    if blog:
        st.markdown(f"## {blog.title}")
        st.caption(f"Saved on {blog.created_at.strftime('%b %d, %Y %H:%M')}")
        st.markdown("---")
        st.write(blog.content)
    else:
        st.error("Blog not found.")
        st.session_state.selected_blog_id = None

else:
    blogs = get_saved_blogs()

    if not blogs:
        st.write("No saved outlines yet.")
    else:
        for blog in blogs:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{blog.title}**")
            with col2:
                st.write(blog.created_at.strftime("%b %d, %Y"))
            with col3:
                if st.button("View", key=f"view_{blog.id}"):
                    st.session_state.selected_blog_id = blog.id
                    st.rerun()
            st.markdown("---")
