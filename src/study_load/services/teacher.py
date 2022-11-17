from sqlmodel import Session
from fastapi import Depends
from src.db import get_session
from typing import List
from src.study_load.models import Teacher
from sqlmodel import Session, select


class TeacherService:
  def __init__(self, session: Session = Depends(get_session)):
    self.session = session

  def get_all(self) -> List[Teacher]:
    result = self.session.execute(select(Teacher))
    teachers = result.scalars().all()
    return teachers

  def create(self, new_teacher: Teacher) -> Teacher:
    teacher = Teacher(**new_teacher.dict())
    self.session.add(teacher)
    self.session.commit()
    self.session.refresh(teacher)

    return teacher