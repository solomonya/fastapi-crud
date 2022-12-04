from fastapi import APIRouter, Depends
from ..services import LoadService, get_current_admin
from ..models import load, Admin
from typing import List

router = APIRouter(
    prefix='/load',
    tags=['Load']
)


@router.get('/{load_id}', response_model=load.LoadRead)
def get_load(service: LoadService = Depends(), load_id: int = 1):
    return service.get_one(load_id)


@router.get('/', response_model=List[load.LoadRead])
def get_loads(
    service: LoadService = Depends(),
    admin: Admin = Depends(get_current_admin)
):
    return service.get_all()


@router.post('/', response_model=load.Load)
def create_load(
    load_data: load.LoadCreate,
    admin: Admin = Depends(get_current_admin),
    service: LoadService = Depends()
):

    return service.create_load(load_data)


@router.delete('/', response_model=dict[str, bool])
def remove_load(
    load_id: int,
    admin: Admin = Depends(get_current_admin),
    service: LoadService = Depends()
):
    return service.remove_load(load_id)
