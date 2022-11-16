from sqlmodel import SQLModel, Field

class DepartmentBase(SQLModel):
  name: str


class Admin(AdminBase, table=True):
  id: int = Field(default=None, primary_key=True)