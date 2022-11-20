from src.study_load.models import Speciality
from typing import List
from sqlmodel import select
from fastapi import Depends, HTTPException
from sqlmodel import Session
from src.db import get_session
from src.study_load.models import SpecialityBase

class SpecialityService:
  def __init__(self, session: Session = Depends(get_session)):
    self.session = session

  def _get(self, speciality_id: int) -> Speciality:
    speciality_db = self.session.get(Speciality, speciality_id)

    if not speciality_db:
      raise HTTPException(status_code=404, detail='Speciality not found')

    return speciality_db

  def get_all(self) -> List[Speciality]:
    departments = self.session.exec(select(Speciality)).all()
    return departments

  def create_speciality(self, speciality_data: SpecialityBase) -> Speciality:
    speciality = Speciality(**speciality_data.dict())
    self.session.add(speciality)
    self.session.commit()
    self.session.refresh(speciality)

    return speciality

  def update_speciality(self, data: Speciality) -> Speciality:
    speciality_db = self._get(data.id)
    speciality_data = data.dict(exclude_unset=True)

    for field, value in speciality_data.items():
      setattr(speciality_db, field, value)

    self.session.add(speciality_db)
    self.session.commit()
    self.session.refresh(speciality_db)

    return speciality_db

  def delete_speciality(self, id: int):
    speciality_db = self._get(id)
    self.session.delete(speciality_db)
    self.session.commit()

    return { "ok": True }
