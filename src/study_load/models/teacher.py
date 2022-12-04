from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List
from datetime import date
from .links import TeacherStudyLoadLink


class TeacherBase(SQLModel):
    last_name: str
    first_name: str
    middle_name: str
    academic_degree: str
    hiring_date: date
    department_id: Optional[int] = Field(
        default=None, foreign_key="department.id")
    position: str
    email: str
    password_hash: str


class Teacher(TeacherBase, table=True):
    id: int = Field(default=None, primary_key=True)
    loads: List['Load'] = Relationship(
        back_populates='teachers', link_model=TeacherStudyLoadLink)
