from app.db.session import SessionLocal
from app.db.models import User

db = SessionLocal()

user = User(
    email="test@client.com",
    api_key="sk_live_test123",
    plan="free",
    monthly_quota=10
)

db.add(user)
db.commit()

db.close()
