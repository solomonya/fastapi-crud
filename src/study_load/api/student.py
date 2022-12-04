from typing import List
from fastapi import APIRouter, Depends
from ..models import StudentBase, Student, Admin
from ..models import student
from ..services import get_current_admin, StudentsService

router = APIRouter(
    prefix='/students',
    tags=['Students']
)


@router.get('/', response_model=List[student.StudentWithGroup])
def get_students(
    admin: Admin = Depends(get_current_admin),
    service: StudentsService = Depends()
):
    return service.get_all()


@router.get('/{student_id}', response_model=student.StudentWithGroup)
def get_student(id: int, admin: Admin = Depends(get_current_admin),
                service: StudentsService = Depends()
                ):
    return service.get_one(id)


@router.post('/', response_model=Student)
def create_student(
    student_data: StudentBase,
    admin: Admin = Depends(get_current_admin),
    service: StudentsService = Depends()
):
    return service.create(student_data)


@router.put('/', response_model=Student)
def update(
    payload: Student,
    admin: Admin = Depends(get_current_admin),
    service: StudentsService = Depends(),
):
    return service.update(payload)


@router.delete('/', response_model=dict[str, bool])
def delete(
    student_id: int,
    admin: Admin = Depends(get_current_admin),
    service: StudentsService = Depends(),
):
    return service.delete(student_id)
