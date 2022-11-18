from sqlmodel import SQLModel, Field

class AdminBase(SQLModel):
  email: str
  password_hash: str


class Admin(AdminBase, table=True):
  id: int = Field(default=None, primary_key=True)