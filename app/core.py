import secrets
from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from app.constants import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = secrets.token_urlsafe(32)


# todo think if need to change subject as id to email
def create_access_token(
    subject: int, expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
