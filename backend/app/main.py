from fastapi import FastAPI
from app.database.connection import engine, Base

from app.models.skills import Skill
from app.models.projects import Project
from app.models.experiences import Experience

from app.routes.skills import router as skills_router
from app.routes.projects import router as projects_router
from app.routes.experiences import router as experience_router

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My Portfolio API",
    description="Backend API for interactive developer portfolio",
    version="1.0.0",
)

app.include_router(skills_router)
app.include_router(projects_router)
app.include_router(experience_router)

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