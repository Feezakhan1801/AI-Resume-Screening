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
<<<<<<< HEAD
=======

# AI Resume Screening System

AI Resume Screening System is a Generative AI based application that automatically evaluates resumes against specific job roles using a Large Language Model (Google Gemini). The system analyzes resume content, compares it with job requirements, and generates a score along with reasoning.

This project uses FastAPI for the backend, Streamlit for the frontend, and SQLite for storing evaluation results.

--------------------------------------------------

## Features

- Upload resumes in PDF or TXT format
- Select job role for evaluation
- AI automatically evaluates the resume
- Generates a score from 0 to 100
- Provides reasoning for the score
- Stores previous evaluations in SQLite database
- Simple and interactive Streamlit interface

--------------------------------------------------

## Project Structure

AI-Resume-Screening-System

backend/
- main.py
- database.py
- llm.py
- resume_parser.py
- roles.py

frontend/
- app.py

resume-data/

.env

requirements.txt

README.md

--------------------------------------------------

## Tech Stack

Backend  
FastAPI  
Python  
SQLite  

Frontend  
Streamlit  

AI / LLM  
Google Gemini API  

Libraries  
PyPDF2  
python-dotenv  
requests  

--------------------------------------------------

## Supported Job Roles

DevOps Engineer

Skills considered:
- CI/CD pipelines
- Docker
- Kubernetes
- Cloud platforms (AWS / GCP / Azure)
- Infrastructure as Code (Terraform, Ansible)
- Linux administration
- Monitoring tools (Prometheus, Grafana)

AI Developer

Skills considered:
- Strong Python programming
- Machine learning frameworks
- LLM / NLP / Computer Vision
- PyTorch / TensorFlow
- Model training and evaluation
- Data preprocessing

MERN Stack Developer

Skills considered:
- MongoDB
- Express.js
- React.js
- Node.js
- REST API development
- Frontend UI development

--------------------------------------------------

## Installation






### 2 Create Virtual Environment

python -m venv venv


Activate virtual environment

Windows

venv\Scripts\activate


Mac / Linux

source venv/bin/activate


### 3 Install Dependencies

pip install -r requirements.txt

--------------------------------------------------

## Environment Setup

Create a `.env` file in the project root directory.

Add your Gemini API key.

GEMINI_API_KEY=your_api_key_here

You can generate the API key from:

https://makersuite.google.com/app/apikey

--------------------------------------------------

# How to Run the Project

You need to run **Backend first**, then **Frontend**.

--------------------------------------------------

## Step 1: Run Backend (FastAPI)

From the project root, start the FastAPI backend:

```bash
uvicorn backend.main:app --reload
```

Backend will start at:

http://localhost:8000

You can check API docs at:

http://localhost:8000/docs

> If you prefer running directly from the `backend/` folder, you can also run:
>
> ```bash
> python backend/main.py
> ```

--------------------------------------------------

## Step 2: Run Frontend (Streamlit)

Open a **new terminal**.

Go to frontend folder.

cd frontend

Run the Streamlit app.

streamlit run app.py

Frontend will open automatically in browser:

http://localhost:8501

--------------------------------------------------

## How to Use the Application

1 Upload a resume (PDF or TXT)

2 Select job role

- DevOps Engineer
- AI Developer
- MERN Stack Developer

3 Click **Evaluate Resume**

4 System will generate

- Resume Score (0–100)
- Reasoning for the score

5 Click **Load Results** to see previous evaluations

--------------------------------------------------

## API Endpoints

Upload Resume

POST /upload-resume

Upload a PDF or TXT resume file.


Evaluate Resume

POST /evaluate-resume

Request Example

{
 "resume_name": "resume.pdf",
 "role": "AI Developer"
}

Response Example

{
 "score": 85,
 "reasoning": "The candidate has strong Python and machine learning experience that aligns with the AI Developer role."
}


Get Previous Results

GET /results

Returns all previous resume evaluations stored in the database.

--------------------------------------------------

## How Resume Evaluation Works

1 User uploads a resume through the Streamlit interface

2 Resume text is extracted from the file

3 Selected job role requirements are retrieved

4 A prompt is sent to the Gemini LLM

5 The LLM evaluates the resume

6 The system generates a score and reasoning

7 Results are stored in SQLite database

--------------------------------------------------

## Example Output

Resume: Rahul Sharma Resume.pdf  
Role: DevOps Engineer  
Score: 92  

Reasoning:
The candidate demonstrates strong experience with Docker, Kubernetes, and AWS which aligns well with the DevOps role requirements.

--------------------------------------------------

## Future Improvements

- Add support for more job roles
- Resume ranking for multiple candidates
- Dashboard for analytics
- Authentication system
- Batch resume evaluation
- Resume keyword highlighting

--------------------------------------------------

## Author

Feeza Pathan

AI / Machine Learning / Generative AI Projects

--------------------------------------------------

>>>>>>> f30fa79 (Initial commit - AI Resume Screening System)
