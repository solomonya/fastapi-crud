from fastapi import APIRouter, Depends
from ..services import LoadService, get_current_admin
from ..models import load, Admin
from typing import List

router = APIRouter(
  prefix='/load',
  tags=['Load']
)

@router.get('/', response_model=List[load.Load])
def get_loads(
  service: LoadService = Depends(),
  admin: Admin = Depends(get_current_admin)
) -> List[load.Load]:
  return service.get_all()


@router.post('/', response_model=load.Load)
def create_load(
  load_data: load.LoadCreate,
  admin: Admin = Depends(get_current_admin),
  service: LoadService = Depends()
) -> load.Load:
  
  return service.create_load(load_data)
