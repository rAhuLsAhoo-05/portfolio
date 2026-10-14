from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.database.connection import get_db
from backend.app.models.skills import Skill
from backend.app.schemas.skills import SkillCreate, SkillResponse


router = APIRouter(
    prefix="/skills",
    tags=["Skills"],
)


@router.post("/", response_model=SkillResponse)
def create_skill(
    skill: SkillCreate,
    db: Session = Depends(get_db),
):
    new_skill = Skill(
        name=skill.name,
        category=skill.category,
        level=skill.level,
    )

    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)

    return new_skill


@router.get("/", response_model=List[SkillResponse])
def get_skills(
    db: Session = Depends(get_db),
):
    return db.query(Skill).all()


@router.get("/{skill_id}", response_model=SkillResponse)
def get_skill(
    skill_id: int,
    db: Session = Depends(get_db),
):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found",
        )

    return skill

@router.put("/{skill_id}", response_model=SkillResponse)
def update_skill(
    skill_id: int,
    skill_data: SkillCreate,
    db: Session = Depends(get_db),
):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found",
        )

    skill.name = skill_data.name
    skill.category = skill_data.category
    skill.level = skill_data.level

    db.commit()
    db.refresh(skill)

    return skill

@router.delete("/{skill_id}")
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found",
        )

    db.delete(skill)
    db.commit()

    return {
        "message": "Skill deleted successfully"
    }