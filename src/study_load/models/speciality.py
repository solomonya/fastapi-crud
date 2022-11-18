from sqlmodel import SQLModel, Field


class SpecialityBase(SQLModel):
    name: str
    code: str


class Speciality(SpecialityBase, table=True):
    id: int = Field(default=None, primary_key=True)

