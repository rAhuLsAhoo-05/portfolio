from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.experiences import Experience
from app.schemas.experiences import ExperienceCreate, ExperienceResponse


router = APIRouter(
    prefix="/experience",
    tags=["Experience"],
)


@router.post("/", response_model=ExperienceResponse)
def create_experience(
    experience: ExperienceCreate,
    db: Session = Depends(get_db),
):
    new_experience = Experience(
        company=experience.company,
        role=experience.role,
        start_date=experience.start_date,
        end_date=experience.end_date,
        description=experience.description,
        technologies=experience.technologies,
    )

    db.add(new_experience)
    db.commit()
    db.refresh(new_experience)

    return new_experience


@router.get("/", response_model=List[ExperienceResponse])
def get_experiences(
    db: Session = Depends(get_db),
):
    return db.query(Experience).all()


@router.get("/{experience_id}", response_model=ExperienceResponse)
def get_experience(
    experience_id: int,
    db: Session = Depends(get_db),
):
    experience = db.query(Experience).filter(
        Experience.id == experience_id
    ).first()

    if not experience:
        raise HTTPException(
            status_code=404,
            detail="Experience not found",
        )

    return experience


@router.put("/{experience_id}", response_model=ExperienceResponse)
def update_experience(
    experience_id: int,
    experience_data: ExperienceCreate,
    db: Session = Depends(get_db),
):
    experience = db.query(Experience).filter(
        Experience.id == experience_id
    ).first()

    if not experience:
        raise HTTPException(
            status_code=404,
            detail="Experience not found",
        )

    experience.company = experience_data.company
    experience.role = experience_data.role
    experience.start_date = experience_data.start_date
    experience.end_date = experience_data.end_date
    experience.description = experience_data.description
    experience.technologies = experience_data.technologies

    db.commit()
    db.refresh(experience)

    return experience


@router.delete("/{experience_id}")
def delete_experience(
    experience_id: int,
    db: Session = Depends(get_db),
):
    experience = db.query(Experience).filter(
        Experience.id == experience_id
    ).first()

    if not experience:
        raise HTTPException(
            status_code=404,
            detail="Experience not found",
        )

    db.delete(experience)
    db.commit()

    return {
        "message": "Experience deleted successfully"
    }