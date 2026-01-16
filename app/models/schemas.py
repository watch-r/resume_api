from pydantic import BaseModel
from typing import List

class ResumeResponse(BaseModel):
    resume_id: str
    language_detected: str
    name: str | None
    email: str | None
    phone: str | None
    skills: List[str]
    experience_years: float | None
