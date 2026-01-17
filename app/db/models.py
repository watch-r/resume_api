from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

SCHEMA_NAME = "resume_api"

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {"schema": SCHEMA_NAME}
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    api_key = Column(String, unique=True, index=True, nullable=False)
    plan = Column(String, nullable=False, default='free')
    monthly_quota = Column(Integer, nullable=False, default=10)   
    used_quota = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    logs = relationship("APILog", back_populates="user")
    
class APILog(Base):
    __tablename__ = 'api_logs'
    __table_args__ = {"schema": SCHEMA_NAME}
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.users.id"))
    endpoint = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="logs")