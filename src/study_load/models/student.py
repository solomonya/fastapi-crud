from sqlmodel import Relationship, SQLModel, Field
from typing import Optional

from src.study_load.models.study_group import Sgroup, SgroupRead


class StudentBase(SQLModel):
    id: int
    last_name: str
    first_name: str
    middle_name: str
    perfomance: float


class Student(StudentBase, table=True):
    id: int = Field(default=None, primary_key=True)
    study_group_id: Optional[int] = Field(
        default=None, foreign_key='sgroup.id')
    study_group: Optional[Sgroup] = Relationship(back_populates='students')


class StudentWithGroup(StudentBase):
    study_group: Optional[SgroupRead]
