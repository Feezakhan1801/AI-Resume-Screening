from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil
from .database import init_db, save_evaluation, get_all_results
from .roles import JOB_ROLES
from .resume_parser import extract_text_from_file
from .llm import evaluate_resume

app = FastAPI()

RESUME_DIR = "../resume-data"

@app.on_event("startup")
def startup_event():
    init_db()
    os.makedirs(RESUME_DIR, exist_ok=True)

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(('.pdf', '.txt')):
        raise HTTPException(status_code=400, detail="Only PDF and TXT files are allowed")
    file_path = os.path.join(RESUME_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "Resume uploaded successfully", "resume_name": file.filename}

@app.post("/evaluate-resume")
async def evaluate_resume_endpoint(data: dict):
    resume_name = data.get("resume_name")
    role = data.get("role")
    if not resume_name or not role:
        raise HTTPException(status_code=400, detail="resume_name and role are required")
    if role not in JOB_ROLES:
        raise HTTPException(status_code=400, detail="Invalid role")
    file_path = os.path.join(RESUME_DIR, resume_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Resume not found")
    resume_text = extract_text_from_file(file_path)
    role_req = JOB_ROLES[role]
    score, reasoning = evaluate_resume(resume_text, role_req)
    save_evaluation(resume_name, role, score, reasoning)
    return {"score": score, "reasoning": reasoning}

@app.get("/results")
async def get_results():
    return get_all_results()