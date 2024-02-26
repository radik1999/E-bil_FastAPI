from pydantic import EmailStr
from sqlmodel import SQLModel, Field, AutoString


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, sa_type=AutoString)
    full_name: str | None = None


class User(UserBase, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str


class UserOut(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(SQLModel):
    sub: int | None = None
