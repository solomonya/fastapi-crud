from fastapi import APIRouter, Depends
from ..models import StudentBase, Student, Admin
from ..services import get_current_admin, StudentsService 
from typing import List

router = APIRouter(
    prefix='/students',
    tags=['Students']
)


@router.get('/', response_model=List[Student])
def get_students(
    admin: Admin = Depends(get_current_admin),
    service: StudentsService = Depends()
):
    return service.get_all()

@router.post('/', response_model=Student)
def create_student(
    student_data: StudentBase, 
    admin: Admin = Depends(get_current_admin),
    service: StudentsService = Depends()
):
    return service.create(student_data)

@router.put('/', response_model = Student)
def update(
    admin: Admin = Depends(get_current_admin)
):
    pass
