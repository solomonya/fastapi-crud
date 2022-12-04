from fastapi import APIRouter, Depends
from ..models import Speciality, Admin, SpecialityBase
from typing import List
from ..services import get_current_admin, SpecialityService

router = APIRouter(
    prefix='/specialities',
    tags=['specialities']
)


@router.get('/{speciality_id}', response_model=Speciality)
def get_speciality(
    speciality_id: int,
    service: SpecialityService = Depends(),
    admin=Depends(get_current_admin),
):
    return service.get_one(speciality_id)


@router.get('/', response_model=List[Speciality])
def get_specialities(
    service: SpecialityService = Depends(),
    admin: Admin = Depends(get_current_admin)
):
    return service.get_all()


@router.post('/', response_model=Speciality)
def create_speciality(
    data: SpecialityBase,
    service: SpecialityService = Depends(),
    admin: Admin = Depends(get_current_admin),
):
    return service.create_speciality(data)


@router.put('/', response_model=Speciality)
def update_speciality(
    data: Speciality,
    service: SpecialityService = Depends(),
    admin: Admin = Depends(get_current_admin)
):
    return service.update_speciality(data)


@router.delete('/', response_model=dict[str, bool])
def delete_speciality(
    id: int,
    service: SpecialityService = Depends(),
    admin: Admin = Depends(get_current_admin)
):
    return service.delete_speciality(id)
