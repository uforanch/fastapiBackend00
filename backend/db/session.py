from collections.abc import Generator
from typing import final

from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker

from core.config import settings



SQLALCHEMY_DATABSE_URL = settings.DATABASE_URL
print("Database Url is ", SQLALCHEMY_DATABSE_URL)
engine = create_engine(SQLALCHEMY_DATABSE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# can now use `db= get_db().__next__()` to get a local db
# can query with db.query(User).all()

