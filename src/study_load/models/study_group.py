from sqlmodel import SQLModel, Field
from typing import Optional


class StudyGroupBase(SQLModel):
    code: str
    name: str
    specialily_id: Optional[int]

class Sgroup(StudyGroupBase, table=True):
    id: int = Field(default=None, primary_key=True)
    specialily_id: Optional[int] = Field(default=None, foreign_key='speciality.id')
