import json
import os
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the repository root .env file (regardless of the current working directory)
ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(dotenv_path=ROOT_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not set. Please add it to your .env file.")

genai.configure(api_key=API_KEY)


def _extract_json(text: str) -> str:
    """Try to extract a JSON object from the LLM output."""
    text = text.strip()
    if text.startswith("{") and text.endswith("}"):
        return text

    # Find first and last braces to isolate JSON
    first = text.find("{")
    last = text.rfind("}")
    if first != -1 and last != -1 and last > first:
        return text[first : last + 1]

    return text


def evaluate_resume(resume_text, role_requirements):
    prompt = f"""
You are an AI recruiter evaluating resumes. Score the resume from 0 to 100 based on how well it matches the job requirements.

Job Role Requirements:
{role_requirements}

Resume Text:
{resume_text}

Provide your response as a JSON object with exactly two keys: "score" (an integer from 0 to 100) and "reasoning" (a short explanation string).
"""

    # Use a supported Gemini model for text generation
    model = genai.GenerativeModel("gemini-2.5-flash")

    try:
        response = model.generate_content(prompt)
    except Exception as exc:
        # Propagate as a structured failure so the API caller can see what happened.
        return 0, f"LLM request failed: {exc}"

    # Different SDK versions may expose the text in different fields.
    result_text = getattr(response, "text", None) or getattr(response, "content", None) or str(response)
    result_text = result_text.strip()

    json_text = _extract_json(result_text)

    try:
        parsed = json.loads(json_text)
        score = int(parsed.get("score", 0))
        reasoning = str(parsed.get("reasoning", ""))
        return score, reasoning
    except Exception:
        # Return a safe default and include the raw output for troubleshooting.
        return 0, f"Error parsing LLM response. Raw output: {result_text}"