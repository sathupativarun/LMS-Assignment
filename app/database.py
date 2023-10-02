# app/database.py
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends, HTTPException, status
from app.models import User

DATABASE_URL = "mongodb://localhost:27017"
DATABASE_NAME = "library"

client = None

async def connect():
    global client
    client = AsyncIOMotorClient(DATABASE_URL)
    db = client[DATABASE_NAME]

async def disconnect():
    client.close()

def get_db():
    return client[DATABASE_NAME]
