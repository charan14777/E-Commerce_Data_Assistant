📌 Project Overview
This project builds a local AI-powered agent that can answer natural language questions based on provided e-commerce datasets. It uses a local Large Language Model (LLM) to translate user queries into SQL, retrieve answers from a structured database, and respond via API. Optional features include data visualization and real-time streaming responses.

🗂️ Dataset Description
You will work with the following three structured CSV datasets:

Product-Level Ad Sales and Metrics
Product-Level Total Sales and Metrics
Product-Level Eligibility Table

All these are converted into SQL tables to facilitate querying.


🎯 Objectives
Build a pipeline to:
Receive user questions via API
Convert natural language to SQL using an LLM
Query the database
Return a user-friendly response

(Bonus)
Add visualizations using Plotly or Matplotlib
Implement event-streamed responses (e.g., live typing effect)


🛠️ Tech Stack
Python 3.10+
SQLite / PostgreSQL (SQLite used for local development)
FastAPI – for building RESTful API
LangChain / Transformers – for integrating LLM
Ollama / GPT4All / LM Studio / Gemini 2.5 API – for LLM support
SQLAlchemy – for ORM + DB connection
Matplotlib / Plotly – for optional data visualization
Uvicorn – for running FastAPI app


📦 Setup Instructions
1. Clone the Repository
2. Install Dependencies
3. Prepare the Dataset
4. Load Data into SQL
5. Start the API
      

