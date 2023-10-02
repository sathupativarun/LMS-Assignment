# app/models.py
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str
    password: str

class Book(BaseModel):
    title: str
    author: str
    genre: str

