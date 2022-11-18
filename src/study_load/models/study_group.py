from sqlmodel import SQLModel, Field
from typing import Optional


class StudyGroupBase(SQLModel):
    code: str
    name: str

class StudyGroup(StudyGroupBase):
    id: int = Field(default=None, primary_key=True)
    specialily_id: Optional[int] = Field(default=None, foreign_key='speciality.id')
