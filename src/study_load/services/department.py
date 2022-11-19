from src.db import get_session
from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from ..models import Department
from typing import List


class DepartmentService:
  def __init__(self, session: Session = Depends(get_session)):
    self.session = session

  def _get(self, department_id :int) -> Department:
    department = self.session.get(Department, department_id)

    if not department:
      raise HTTPException(status_code=404, detail='Department not found')

    return department

  def get_all(self) -> List[Department]:
    result = self.session.execute(select(Department))
    departments = result.scalars().all()
    return departments

  def create_department(self, department_data) -> Department:
    department = Department(**department_data.dict())
    self.session.add(department)
    self.session.commit()
    self.session.refresh(department)

    return department

  def update_department(self, department: Department) -> Department:
    department_db = self._get(department.id)
    department_data = department.dict(exclude_unset=True)

    for field, value in department_data.items():
      setattr(department_db, field, value)

    self.session.add(department_db)
    self.session.commit()
    self.session.refresh(department_db)

    return department_db

  def delete_department(self, department_id: int):
    department_db = self._get(department_id)
    self.session.delete(department_db)
    self.session.commit()

    return { "ok": True }