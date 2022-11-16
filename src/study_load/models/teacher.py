from sqlmodel import SQLModel, Field

class TeacherBase(SQLModel):
  name: str
  academic_degree: str
  position: str

class Teacher(TeacherBase, table=True):
  id: int = Field(default=None, primary_key=True)