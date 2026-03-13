import streamlit as st
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

if "OPENAI_API_KEY" not in os.environ:
    st.error("Please set your OpenAI API key in your .env file.")
    
model = "gpt-4.1"

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def get_blog_outline(topic, target_audience, seo_keywords, tone, blog_length):
    """
    Generates a blog outline using OpenAI Chat API and returns JSON with 'title' and 'content'.
    """
    prompt = f"""
    You are an expert content writer and blogger with over 15 years of experience in creating high-quality, engaging, and SEO-optimized blog posts. 
    Write a complete blog post based on the information below. 
    The blog should be fully written in one go and match the expected blog length, with a clear introduction, informative body, and a strong conclusion. 
    Use the target audience, tone, and primary SEO keywords appropriately.

    Topic: {topic}
    Target Audience: {target_audience}
    Primary SEO Keywords: {seo_keywords}
    Tone: {tone}
    Expected Blog Length: {blog_length} words

    Please provide the output strictly in JSON format with the following keys:
    {{
        "title": "The blog post title",
        "content": "The full blog post content including introduction, body, and conclusion. Make the content approximately {blog_length} words long."
    }}
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
        
    raw_output = response.choices[0].message.content.strip()

    try:
        result = json.loads(raw_output)
    except json.JSONDecodeError:
        result = {"title": topic, "content": raw_output}
    
    return result
