from fastapi import FastAPI


app = FastAPI(
    title="Resume Parser API",
    description="An API to parse resumes and extract relevant information.",
    version="1.0.0",
)


@app.get("/")
def health_check():
    return {"status": "ok"}