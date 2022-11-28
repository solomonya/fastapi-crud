from fastapi import Depends, APIRouter
from ..models import Discipline, DisciplineBase, Admin
from typing import List
from ..services import DisciplineService
from ..services import get_current_admin

router = APIRouter(
  prefix='/discipline',
  tags=['Discipline']
)


@router.get('/', response_model = List[Discipline])
def get_departments(
  service: DisciplineService = Depends(),
  admin: Admin = Depends(get_current_admin)
  ):
  return service.get_all()


@router.post('/', response_model=Discipline)
def create_department(
  discipline_data: DisciplineBase,
  service: DisciplineService = Depends(),
  admin: Admin = Depends(get_current_admin),
):
  return service.create_discipline(discipline_data)

@router.put('/')
def update_disciplines(
  discipline_data: Discipline,
  service: DisciplineService = Depends(),
  admin: Admin = Depends(get_current_admin)
):
  return service.update_discipline(discipline_data)


@router.delete('/', response_model = dict[str, bool])
def delete_discipline(
  discipline_id: int,
  service: DisciplineService = Depends(),
  admin: Admin = Depends(get_current_admin)
  ):
  return service.delete_discipline(discipline_id)
