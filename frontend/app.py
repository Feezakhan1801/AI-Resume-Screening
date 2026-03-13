import streamlit as st
import requests
import os

BACKEND_URL = "http://localhost:8000"

st.title("AI Resume Screening System")

uploaded_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])
role = st.selectbox("Select Job Role", ["DevOps Engineer", "AI Developer", "MERN Stack Developer"])

if st.button("Evaluate Resume"):
    if uploaded_file is not None and role:
        # Upload file
        files = {"file": uploaded_file}
        upload_response = requests.post(f"{BACKEND_URL}/upload-resume", files=files)
        if upload_response.status_code == 200:
            resume_name = upload_response.json()["resume_name"]
            # Evaluate
            eval_data = {"resume_name": resume_name, "role": role}
            eval_response = requests.post(f"{BACKEND_URL}/evaluate-resume", json=eval_data)
            if eval_response.status_code == 200:
                result = eval_response.json()
                st.success(f"Score: {result['score']}/100")
                st.write(f"Reasoning: {result['reasoning']}")
            else:
                st.error("Evaluation failed")
        else:
            st.error("Upload failed")
    else:
        st.error("Please upload a file and select a role")

st.header("Previous Evaluations")
if st.button("Load Results"):
    results_response = requests.get(f"{BACKEND_URL}/results")
    if results_response.status_code == 200:
        results = results_response.json()
        for res in results:
            st.write(f"Resume: {res['resume_name']}, Role: {res['role']}, Score: {res['score']}, Reasoning: {res['reasoning']}")
    else:
        st.error("Failed to load results")