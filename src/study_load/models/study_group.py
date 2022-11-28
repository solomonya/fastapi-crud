from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List
from .load import Load
from .links import GroupStudyLoadLink


class StudyGroupBase(SQLModel):
    code: str
    name: str
    speciality_id: Optional[int]

class Sgroup(StudyGroupBase, table=True):
    id: int = Field(default=None, primary_key=True)
    speciality_id: Optional[int] = Field(default=None, foreign_key='speciality.id')

    load: List[Load] = Relationship(back_populates='sgroup', link_model=GroupStudyLoadLink)
