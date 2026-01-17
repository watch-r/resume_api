from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.core.security import verify_api_key, get_db
from app.core.rate_limit import log_usage
from app.services.resume_parser import extract_text_from_pdf, parse_resume_text
from app.db.models import User

router = APIRouter()

@router.post("/parse")
async def parse_resume(
    file: UploadFile = File(...),
    user: User = Depends(verify_api_key),
    db: Session = Depends(get_db)
):
    text = extract_text_from_pdf(file.file)
    parsed = parse_resume_text(text)

    log_usage(db, user, "/v1/resume/parse")

    return parsed
