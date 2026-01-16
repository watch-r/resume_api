from fastapi import Header, HTTPException, status
from app.core.config import API_KEY_HEADER

# TEMP: replace with DB lookup later
VALID_API_KEYS = {
    "sk_test_123456"
}

def verify_api_key(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid auth header"
        )

    api_key = authorization.replace("Bearer ", "")

    if api_key not in VALID_API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key"
        )

    return api_key
