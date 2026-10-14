from sqlalchemy import Column, Integer, String, Text

from app.database.connection import Base


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    title = Column(String, nullable=False)

    bio = Column(Text, nullable=False)

    location = Column(String, nullable=True)

    email = Column(String, nullable=True)

    phone = Column(String, nullable=True)

    github_url = Column(String, nullable=True)

    linkedin_url = Column(String, nullable=True)

    resume_url = Column(String, nullable=True)