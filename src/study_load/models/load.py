from sqlmodel import Relationship, SQLModel, Field

from ..models.discipline import Discipline
from ..models.teacher import Teacher
from ..models.study_group import Sgroup
from . import links
from typing import List


class LoadCreate(SQLModel):
    discipline_id: int
    teachers: List[int]
    groups: List[int]


class LoadBase(SQLModel):
    id: int
    discipline: Discipline


class Load(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None)
    discipline_id: int = Field(foreign_key='discipline.id')
    discipline: Discipline = Relationship(
        back_populates='load'
    )

    teachers: List['Teacher'] = Relationship(
        back_populates="loads", link_model=links.TeacherStudyLoadLink)
    sgroups: List['Sgroup'] = Relationship(
        back_populates='loads', link_model=links.GroupStudyLoadLink)


class LoadRead(LoadBase):
    teachers: List[Teacher] = []
    sgroups: List[Sgroup] = []
