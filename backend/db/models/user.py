from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

#had to kill alembic version and do new first because a line of code in alembic

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    blogs = relationship("Blog",back_populates="author")