from fastapi import APIRouter, UploadFile, File
from app.services.recommendation_engine import generate_recommendations
import os

from app.services.resume_parser import extract_text_from_pdf, extract_text_from_docx
from app.services.skill_extractor import extract_skills, extract_experience
from app.services.matching_engine import match_jobs

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename.endswith((".pdf", ".docx")):
        return {"error": "Only PDF and DOCX files allowed"}

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_docx(file_path)

    skills = extract_skills(text)
    experience = extract_experience(text)
    matches = match_jobs(skills, experience)
    recommendations = generate_recommendations(matches)

    return {
        "message": "Resume processed successfully",
        "filename": file.filename,
        "skills_found": skills,
        "experience_years": experience,
        "job_matches": matches,
        "recommendations": recommendations,
        "extracted_text_preview": text[:300],
    }
