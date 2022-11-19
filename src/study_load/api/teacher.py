from fastapi import APIRouter, Depends
from typing import List
from ..models import Teacher
from ..services import TeacherService

router = APIRouter(
  prefix='/teachers',
  tags=['teachers']
)

@router.get('/', response_model = List[Teacher])
def get_teachers(service: TeacherService = Depends()):
  return service.get_all()


@router.post('/', response_model = Teacher)
def add_teacher(new_teacher: Teacher, service: TeacherService = Depends()):
  return service.create(new_teacher)