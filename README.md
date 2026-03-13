📝 Blog AI Generator
====================

An AI-powered application built with **Streamlit** to generate, refine, and manage SEO-optimized blog outlines and content using OpenAI.

### 🚀 Getting Started

Follow these steps to set up the project locally using uv for fast dependency management.

#### 1\. Clone the Repository

Open your terminal and run:**git clone cd**

#### 2\. Configure Environment Variables

Create a **.env** file in the root directory and add your OpenAI API key:**cp .env.example .env**

Open **.env** and fill in your key:**OPENAI\_API\_KEY=your\_sk\_key\_here**

#### 3\. Install Dependencies

This project uses **uv** for efficient environment management. Sync the project dependencies by running:**uv sync**

#### 4\. Run the Application

Start the Streamlit server:**uv run streamlit run app.py**

### 🛠️ Tech Stack

*   **Frontend:** Streamlit
    
*   **AI Logic:** OpenAI GPT Models
    
*   **Database:** SQLAlchemy (SQLite)
    
*   **Package Manager:** uv