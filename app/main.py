from fastapi import FastAPI
from app.api.v1 import routes_resume, routes_job_match

app = FastAPI(
    title="Resume Parser API",
    version="1.0.0"
)

app.include_router(routes_resume.router, prefix="/v1/resume", tags=["Resume"])
app.include_router(routes_job_match.router, prefix="/v1/resume", tags=["Job Match"])

@app.get("/")
def health_check():
    return {"status": "ok"}
