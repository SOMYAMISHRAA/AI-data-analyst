from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.database.dependencies import get_db

app=FastAPI(
    title="AI Data Analyst API",
    description="An AI-powered agent that analyzes databases using natural language.",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message":"welcome to AI Data Analyst API",
        "status":"running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application":"AI Data Analyst"
    }

@app.get("/database-check")
def database_check(db:Connection = Depends(get_db)):
    result=db.execute(text("SELECT current_database()"))

    database_name=result.scalar()

    return{
        "message":"database connected successfully",
        "database":database_name

    }
