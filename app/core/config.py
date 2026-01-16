import os

API_KEY_HEADER = "Authorization"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5432/resume_api"
)
