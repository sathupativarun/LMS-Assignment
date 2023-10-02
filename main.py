# main.py
from fastapi import FastAPI
from app import authentication, book, database

app = FastAPI()

# Dependency to get the MongoDB client
@app.on_event("startup")
async def startup_db_client():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await database.disconnect()

# Include routers
app.include_router(authentication.router)
app.include_router(book.router)
