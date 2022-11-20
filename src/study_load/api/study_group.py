from fastapi import APIRouter, Depends
from ..models import Admin, Sgroup, StudyGroupBase
from ..services import get_current_admin, StudyGroupService
from typing import List 


router = APIRouter(
    tags=['Study group'],
    prefix='/study-group',
)

@router.get('/', response_model=List[Sgroup])
def get_study_groups(
    admin: Admin = Depends(get_current_admin),
    service: StudyGroupService = Depends()
):
    return service.get_all()

@router.post('/', response_model = Sgroup)
def create_study_group(
    data:StudyGroupBase,
    admin: Admin = Depends(get_current_admin),
    service: StudyGroupService = Depends()
):
    return service.create(data)

@router.put('/', response_model = Sgroup)
def update_study_group(
    data: Sgroup,
    admin: Admin = Depends(get_current_admin),
    service: StudyGroupService = Depends()
):
    return service.update(data)

@router.delete('/', response_model = dict[str, bool])
def delete_study_group(
    id: int,
    admin: Admin = Depends(get_current_admin), 
    service: StudyGroupService = Depends()
):
    return service.delete(id)
