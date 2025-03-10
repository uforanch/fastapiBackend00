from passlib.context import CryptContext
from sqlalchemy.util import deprecated
import logging

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
logging.getLogger('passlib').setLevel(logging.ERROR) # bcrypt/passlib isn't updated anymore YAAAAAAY


class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)


