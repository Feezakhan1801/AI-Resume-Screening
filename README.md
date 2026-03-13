# AI Resume Screening System

This is a simple AI-powered resume screening system built with Python, FastAPI, Streamlit, SQLite, and Gemini LLM.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Ensure you have Python 3.10.

3. The API key is already set in .env.

## Running the Application

1. Start the backend (FastAPI):
   ```
   uvicorn backend.main:app --reload
   ```
   This will run on http://localhost:8000

2. In a new terminal, start the frontend (Streamlit):
   ```
   streamlit run frontend/app.py
   ```
   This will open the UI in your browser.

## Usage

- Upload a resume (PDF or TXT).
- Select a job role.
- Click Evaluate to get score and reasoning.
- View previous evaluations by clicking Load Results.
