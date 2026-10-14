from sqlalchemy import Column, Integer, String, Text

from app.database.connection import Base


class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String, nullable=False)

    role = Column(String, nullable=False)

    start_date = Column(String, nullable=False)

    end_date = Column(String, nullable=True)

    description = Column(Text, nullable=False)

    technologies = Column(String, nullable=False)