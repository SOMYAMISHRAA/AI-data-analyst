from fastapi import FastAPI

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


