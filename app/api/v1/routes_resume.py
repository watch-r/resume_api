from fastapi import APIRouter, Depends, UploadFile, File
from app.core.security import verify_api_key
from app.services.resume_parser import extract_text_from_pdf, parse_resume_text

router = APIRouter()

@router.post("/parse")
async def parse_resume(
    file: UploadFile = File(...),
    api_key: str = Depends(verify_api_key)
):
    contents = await file.read()
    text = extract_text_from_pdf(file.file)

    parsed = parse_resume_text(text)
    return parsed
