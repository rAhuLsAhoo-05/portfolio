from pydantic import BaseModel
from typing import Optional


class ProjectBase(BaseModel):
    title:str
    description:str
    technologies:str
    github_url:Optional[str] = None
    live_url:Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id:int

    class Config:
        from_attributes = True