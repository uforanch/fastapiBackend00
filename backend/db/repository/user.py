from sqlalchemy.orm import Session

from schemas.user import UserCreate
from db.models.user import User
from core.hashing import Hasher
from datetime import datetime

def create_new_user(user:UserCreate, db:Session):
    user = User(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
        created_at=datetime.now()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user