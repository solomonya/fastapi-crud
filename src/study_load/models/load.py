from sqlmodel import Relationship, SQLModel, Field
from . import links
from typing import List, Optional


class LoadCreate(SQLModel):
    discipline_id: int
    teachers: List[int]
    groups: List[int]

class Load(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None)
    discipline_id: Optional[int] = Field(default=None, foreign_key='discipline.id')

    teacher:List['Teacher']  = Relationship(back_populates="load", link_model=links.TeacherStudyLoadLink)
    sgroup:List['Sgroup'] = Relationship(back_populates='load', link_model=links.GroupStudyLoadLink)
