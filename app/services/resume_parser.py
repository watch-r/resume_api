import pdfplumber
import uuid
import re

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def parse_resume_text(text: str):
    email = re.findall(r"[\\w.-]+@[\\w.-]+", text)
    phone = re.findall(r"\\+?88?01[3-9]\\d{8}", text)

    skills = []
    for skill in ["Python", "FastAPI", "SQL", "React"]:
        if skill.lower() in text.lower():
            skills.append(skill)

    return {
        "resume_id": f"res_{uuid.uuid4().hex[:6]}",
        "language_detected": "en",
        "name": None,
        "email": email[0] if email else None,
        "phone": phone[0] if phone else None,
        "skills": skills,
        "experience_years": None
    }
