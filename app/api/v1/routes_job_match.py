from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.security import verify_api_key, get_db
from app.core.rate_limit import log_usage
from app.services.job_matcher import match_resume_to_job
from app.db.models import User

router = APIRouter()

class JobMatchRequest(BaseModel):
    resume_text: str
    job_description: str

@router.post("/job-match")
def job_match(
    data: JobMatchRequest,
    user: User = Depends(verify_api_key),
    db: Session = Depends(get_db)
):
    score = match_resume_to_job(
        data.resume_text,
        data.job_description
    )

    log_usage(db, user, "/v1/resume/job-match")

    return {"match_score": score}
