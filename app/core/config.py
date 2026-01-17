import os

API_KEY_HEADER = "Authorization"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://mahmud:mahmud@172.21.104.242:5432/resume_api_db"
)
