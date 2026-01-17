from fastapi import Header, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_api_key(
    authorization: str = Header(...),
    db: Session = Depends(get_db)
):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")

    api_key = authorization.replace("Bearer ", "")

    user = db.query(User).filter(User.api_key == api_key).first()

    if not user:
        raise HTTPException(status_code=403, detail="Invalid API key")

    if user.used_quota >= user.monthly_quota:
        raise HTTPException(
            status_code=429,
            detail="Monthly quota exceeded"
        )

    return user
