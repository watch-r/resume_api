from sqlalchemy.orm import Session
from app.db.models import APILog, User

def log_usage(db: Session, user: User, endpoint: str):
    log = APILog(
        user_id=user.id,
        endpoint=endpoint
    )
    user.used_quota += 1

    db.add(log)
    db.commit()
