from sqlmodel import SQLModel, Field
from typing import Optional


class StudentBase(SQLModel):
  last_name: str
  first_name: str
  middle_name: str
  perfomance: float
  study_group_id: int


class Student(StudentBase, table=True):
  id: int = Field(default = None, primary_key = True)
  study_group_id: Optional[int] = Field(default = None, foreign_key='sgroup.id')
