from fastapi import Depends, APIRouter
from ..models import Department, Admin, DepartmentBase
from typing import List
from ..services import DepartmentService
from ..services import get_current_admin

router = APIRouter(
  prefix='/department',
  tags=['department']
)


@router.get('/', response_model = List[Department])
def get_departments(
  service: DepartmentService = Depends(),
  admin: Admin = Depends(get_current_admin)
  ):
  return service.get_all()


@router.post('/', response_model=Department)
def create_department(
  department_data: DepartmentBase,
  service: DepartmentService = Depends(),
  admin: Admin = Depends(get_current_admin),
):
  return service.create_department(department_data)

@router.put('/')
def update_department(
  department_data: Department,
  service: DepartmentService = Depends(),
  admin: Admin = Depends(get_current_admin)
):
  return service.update_department(department_data)


@router.delete('/', response_model = dict[str, bool])
def delete_department(
  department_id: int,
  service: DepartmentService = Depends(),
  admin: Admin = Depends(get_current_admin)
  ):
  return service.delete_department(department_id)