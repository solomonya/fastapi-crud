from fastapi import Depends, HTTPException
from src.db import get_session
from sqlmodel import Session, select
from ..models import Student, StudentBase
from typing import List

class StudentsService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def _get(self, student_id: int) -> Student:
        student = self.session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail='Study group not found')

        return student

    def get_all(self) -> List[Student]:
       students = self.session.exec(select(Student)).all()
       return students

    def create(self, data: StudentBase) -> Student:
      student = Student(**data.dict())
      self.session.add(student)
      self.session.commit()
      self.session.refresh(student)

      return student

    def update(self, data: Student) -> Student:
       student_db = self._get(data.id)
       student_data = data.dict(exclude_unset=True)

       for field, value in student_data.items():
           setattr(student_db, field, value)

       self.session.add(student_db)
       self.session.commit()
       self.session.refresh(student_db)

       return self._get(data.id)

    def delete(self, student_id: int) -> dict[str, bool]:
        student_db = self._get(student_id)
        self.session.delete(student_db)
        self.session.commit()

        return {"success": True}


