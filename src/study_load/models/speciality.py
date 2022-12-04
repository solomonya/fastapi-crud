from sqlmodel import SQLModel, Field, Relationship
from typing import List


class SpecialityBase(SQLModel):
    name: str
    code: str


class Speciality(SpecialityBase, table=True):
    id: int = Field(default=None, primary_key=True)
    study_groups: List['Sgroup'] = Relationship(back_populates='speciality')
