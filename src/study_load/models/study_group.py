from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List
from .links import GroupStudyLoadLink
from .speciality import Speciality, SpecialityBase


class StudyGroupBase(SQLModel):
    code: str
    name: str
    speciality_id: Optional[int]


class Sgroup(StudyGroupBase, table=True):
    id: int = Field(default=None, primary_key=True)
    speciality_id: Optional[int] = Field(
        default=None, foreign_key='speciality.id')

    loads: List['Load'] = Relationship(
        back_populates='sgroups', link_model=GroupStudyLoadLink)
    students: List['Student'] = Relationship(back_populates='study_group')
    speciality: Speciality = Relationship(back_populates='study_groups')


class SgroupRead(SQLModel):
    code: str
    name: str
    speciality: SpecialityBase
