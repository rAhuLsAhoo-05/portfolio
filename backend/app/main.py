from fastapi import FastAPI
from app.database.connection import engine, Base
from backend.app.models.skills import Skill
from app.routes.skills import router as skills_router

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My Portfolio API",
    description="Backend API for interactive developer portfolio",
    version="1.0.0",
)

app.include_router(skills_router)

@app.get("/")
def root():
    return {
        "message":"API running successfully",
        "status":"online"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }