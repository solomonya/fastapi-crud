from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List
from .discipline import Discipline
from .teacher import Teacher
from .study_group import Sgroup


class TeacherStudyLoadLink(SQLModel, table=True):
    study_load_id:Optional[int] = Field(
        default=None, foreign_key="load.id",
        primary_key=True
    )

    teacher_id:Optional[int] = Field(
        default=None, foreign_key="teacher.id",
        primary_key=True
    )

class Load(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None)
    discipline_id: int = Field(foreign_key='discipline.id')

    teachers:List[Teacher] = Relationship(back_populates="teachers", link_model=TeacherStudyLoadLink)
