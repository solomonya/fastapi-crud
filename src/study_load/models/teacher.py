from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class TeacherBase(SQLModel):
  last_name: str
  first_name: str
  middle_name: str
  academic_degree: str
  hiring_date: date
  position: str
  email: str
  password_hash: str

class Teacher(TeacherBase, table=True):
  id: int = Field(default=None, primary_key=True)
  department_id: Optional[int] = Field(default=None, foreign_key="department.id")