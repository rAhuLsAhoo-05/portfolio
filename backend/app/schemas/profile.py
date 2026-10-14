from typing import Optional

from pydantic import BaseModel


class ProfileBase(BaseModel):
    name: str
    title: str
    bio: str
    location: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    github_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    resume_url: Optional[str] = None


class ProfileCreate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    id: int

    class Config:
        from_attributes = True