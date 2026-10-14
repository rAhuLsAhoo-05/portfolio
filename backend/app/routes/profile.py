from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.profile import Profile
from app.schemas.profile import ProfileCreate, ProfileResponse


router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
)


@router.post("/", response_model=ProfileResponse)
def create_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
):
    existing_profile = db.query(Profile).first()

    if existing_profile:
        raise HTTPException(
            status_code=400,
            detail="Profile already exists",
        )

    new_profile = Profile(
        name=profile.name,
        title=profile.title,
        bio=profile.bio,
        location=profile.location,
        email=profile.email,
        phone=profile.phone,
        github_url=profile.github_url,
        linkedin_url=profile.linkedin_url,
        resume_url=profile.resume_url,
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return new_profile


@router.get("/", response_model=ProfileResponse)
def get_profile(
    db: Session = Depends(get_db),
):
    profile = db.query(Profile).first()

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found",
        )

    return profile


@router.put("/", response_model=ProfileResponse)
def update_profile(
    profile_data: ProfileCreate,
    db: Session = Depends(get_db),
):
    profile = db.query(Profile).first()

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found",
        )

    profile.name = profile_data.name
    profile.title = profile_data.title
    profile.bio = profile_data.bio
    profile.location = profile_data.location
    profile.email = profile_data.email
    profile.phone = profile_data.phone
    profile.github_url = profile_data.github_url
    profile.linkedin_url = profile_data.linkedin_url
    profile.resume_url = profile_data.resume_url

    db.commit()
    db.refresh(profile)

    return profile