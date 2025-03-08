from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker

from core.config import settings

SQLALCHEMY_DATABSE_URL = settings.DATABASE_URL
print("Database Url is ", SQLALCHEMY_DATABSE_URL)
engine = create_engine(SQLALCHEMY_DATABSE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)