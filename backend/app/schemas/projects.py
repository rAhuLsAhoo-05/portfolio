from pydantic import BaseModel


class ProjectBase(BaseModel):
    title:str
    description:str
    technologies:str
    github_url:str | None = None
    live_url:str | None = None

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id:int

    class Config:
        from_attributes = True