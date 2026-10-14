from typing import Optional

from pydantic import BaseModel


class ExperienceBase(BaseModel):
    company: str
    role: str
    start_date: str
    end_date: Optional[str] = None
    description: str
    technologies: str


class ExperienceCreate(ExperienceBase):
    pass


class ExperienceResponse(ExperienceBase):
    id: int

    class Config:
        from_attributes = True