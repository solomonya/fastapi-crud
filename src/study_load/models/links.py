from sqlmodel import SQLModel, Field
from typing import Optional

class TeacherStudyLoadLink(SQLModel, table=True):
    study_load_id:Optional[int] = Field(
        default=None, foreign_key="load.id",
        primary_key=True
    )

    teacher_id:Optional[int] = Field(
        default=None, foreign_key="teacher.id",
        primary_key=True
    )

class GroupStudyLoadLink(SQLModel, table=True):
    study_load_id: Optional[int] = Field(
        default=None, foreign_key='load.id',
        primary_key=True
    )

    group_id: Optional[int] = Field(
        default=None, foreign_key='sgroup.id',
        primary_key=True
    )


