from pydantic import BaseModel, Field
from typing import Optional


class Song(BaseModel):
    title: str = Field(max_length=100)
    author: str
    description: Optional[str] = Field(None)
    length: float
    link: str


class SongCreate(BaseModel):
    title: str = Field(max_length=100)
    description: Optional[str] = Field(None)


class SongUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class SongResponse(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    length: float
    link: str
