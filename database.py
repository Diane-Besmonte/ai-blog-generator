import streamlit as st
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone

conn = st.connection("sql", type="sql")

Base = declarative_base()

class SavedBlog(Base):
    __tablename__ = "saved_blogs"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<SavedBlog(id={self.id}, title={self.title}, content={self.content}, created_at={self.created_at})>"


def create_database_table():
    """Create the database table if it doesn't exist."""
    Base.metadata.create_all(bind=conn.engine)
    # st.success("Database tables ensured to exist.")
    

def save_blog(title: str, content: str):
    """Save a generated blog post to the database."""
    Session = sessionmaker(bind=conn.engine)
    session = Session()
    try:
        blog = SavedBlog(title=title, content=content)
        session.add(blog)
        session.commit()
        st.success(f"Blog '{title}' saved to the database!")
    except SQLAlchemyError as e:
        session.rollback()
        st.error(f"Failed to save blog: {e}")
    finally:
        session.close()


def get_saved_blogs():
    """Get all saved blogs from the database."""
    Session = sessionmaker(bind=conn.engine)
    session = Session()
    blogs = session.query(SavedBlog).order_by(SavedBlog.created_at.desc()).all()
    session.close()
    return blogs


def get_blog_by_id(blog_id: int):
    """Get a saved blog by its ID."""
    Session = sessionmaker(bind=conn.engine)
    session = Session()
    
    try:
        blog = session.query(SavedBlog).filter(SavedBlog.id == blog_id).first()
        return blog
    except SQLAlchemyError as e:
        st.error(f"Error fetching blog: {e}")
        return None
    finally:
        session.close()


create_database_table()
