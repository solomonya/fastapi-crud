from fastapi import Depends, APIRouter
from ..models import Department
from typing import List
from ..services import DepartmentService

router = APIRouter(
  prefix='/department'
)


@router.get('/', response_model = List[Department])
def get_departments(service: DepartmentService = Depends()):
  return service.get()