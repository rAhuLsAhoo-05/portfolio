from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.projects import Project
from app.schemas.projects import ProjectCreate, ProjectResponse

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)

@router.post("/",response_model=ProjectResponse)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
):
    new_project = Project(
        title=project.title,
        description=project.description,
        technologies=project.technologies,
        github_url=project.github_url,
        live_url=project.live_url,
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project

@router.get("/",response_model=List[ProjectResponse])
def get_project(
    project_id:int,
    db: Session=Depends(get_db)
):
    return db.query(Project).all()

@router.put("/{project_id}",response_model=ProjectResponse)
def update_project(
    project_id:int,
    project_data:ProjectCreate,
    db: Session=Depends(get_db)
):
    project=db.query(Project).filter(Project.id==project_id).first()
    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )
    project.title=project_data.title
    project.description=project_data.description
    project.technologies=project_data.technologies
    project.github_url=project_data.github_url
    project.live_url=project_data.live_url

    db.commit()
    db.refresh(project)

    return project

@router.delete("/{project_id}")
def delete_project(
    project_id:int,
    db: Session=Depends(get_db)
):
    project=db.query(Project).filter(Project.id==project_id).first()
    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )
    db.delete(project)
    db.commit()

    return {"message":"Project deleted successfully"}