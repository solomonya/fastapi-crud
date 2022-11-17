from sqlmodel import SQLModel, Field
from typing import Optional

class DepartmentBase(SQLModel):
  name: str


class Department(DepartmentBase, table=True):
  id: int = Field(default=None, primary_key=True)

  admin_id:Optional[int] = Field(default=None, foreign_key="admin.id")