from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.security import verify_api_key
from app.services.job_matcher import match_resume_to_job

router = APIRouter()

class JobMatchRequest(BaseModel):
    resume_text: str
    job_description: str

@router.post("/job-match")
def job_match(
    data: JobMatchRequest,
    api_key: str = Depends(verify_api_key)
):
    score = match_resume_to_job(
        data.resume_text,
        data.job_description
    )

    return {
        "match_score": score
    }
