from fastapi import APIRouter, Depends

from src.study_load.services.student import StudentsService
from ..models import Admin, Sgroup, StudyGroupBase, Speciality
from ..services import get_current_admin, StudyGroupService
from typing import List


router = APIRouter(
    tags=['Study group'],
    prefix='/study-group',
)


@router.get('/{study_group_id}', response_model=Sgroup)
def get_study_group(
    study_group_id: int,
    admin=Depends(get_current_admin),
    service: StudyGroupService = Depends(),

):
    return service.get_one(study_group_id)


@router.get('/')
def get_study_groups(
    admin: Admin = Depends(get_current_admin),
    service: StudyGroupService = Depends()
):
    return service.get_all()


@router.post('/', response_model=Sgroup)
def create_study_group(
    data: StudyGroupBase,
    admin: Admin = Depends(get_current_admin),
    service: StudyGroupService = Depends()
):
    return service.create(data)


@router.put('/', response_model=Sgroup)
def update_study_group(
    data: Sgroup,
    admin: Admin = Depends(get_current_admin),
    service: StudyGroupService = Depends()
):
    return service.update(data)


@router.delete('/', response_model=dict[str, bool])
def delete_study_group(
    id: int,
    admin: Admin = Depends(get_current_admin),
    service: StudyGroupService = Depends()
):
    return service.delete(id)
