from fastapi import Depends, HTTPException
from src.db import get_session
from sqlmodel import Session, select
from ..models import student


class StudentsService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def _get(self, student_id: int) -> student.Student:
        student_db = self.session.get(student.Student, student_id)
        if not student_db:
            raise HTTPException(
                status_code=404, detail='Study group not found')

        return student_db

    def get_one(self, id: int):
        return self._get(id)

    def get_all(self):
        students = self.session.exec(select(student.Student)).all()

        return students

    def create(self, data: student.StudentBase) -> student.Student:
        student_db = student.Student(**data.dict())
        self.session.add(student_db)
        self.session.commit()
        self.session.refresh(student_db)

        return student_db

    def update(self, data: student.Student) -> student.Student:
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
