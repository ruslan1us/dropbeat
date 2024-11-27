from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class User(BaseModel):
    email: EmailStr = Field(max_length=100)
    username: str
    password: str


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
