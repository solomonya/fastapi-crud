from sqlmodel import SQLModel, Field
from typing import Optional

class DisciplineBase(SQLModel):
  name: str
  lection_hours: int
  practice_hours: int
  credits: int
  semester: int
  course: int
  rgr_amount: int
  srsp_hours: int


class Discipline(DisciplineBase, table=True):
  id: int = Field(default=None, primary_key=True)
  department_id: Optional[int] = Field(default=None, foreign_key='department.id')
