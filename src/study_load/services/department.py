from src.db import get_session
from fastapi import Depends
from sqlmodel import Session, select
from ..models import Department
from typing import List

class DepartmentService:
  def __init__(self, session: Session = Depends(get_session)):
    self.session = session

  def get(self) -> List[Department]:
    result = self.session.execute(select(Department))
    departments = result.scalars().all()
    return departments