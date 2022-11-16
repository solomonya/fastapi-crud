from fastapi import APIRouter, Depends
from ..models.teacher import Teacher
from typing import List
from sqlmodel import Session, select
from src.db.db import get_session

router = APIRouter(
  prefix='/teachers'
)

@router.get('/teachers', response_model = List[Teacher])
def get_teacher(session: Session = Depends(get_session)):
  result = session.execute(select(Teacher))
  teachers = result.scalars().all()
  return [Teacher(name=teacher.name, academic_degree=teacher.academic_degree, position=teacher.position, id=teacher.id) for teacher in teachers]


@router.post('/teachers')
def add_teacher(teacher: Teacher, session: Session = Depends(get_session)):
  teacher = Teacher(
    name=teacher.name,
    academic_degree=teacher.academic_degree,
    position=teacher.position
  )
  session.add(teacher)
  session.commit()
  session.refresh(teacher)
  return teacher