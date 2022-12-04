from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm


from src.study_load.services.teacher import get_current_teacher
from .. import models
from ..services import TeacherService

router = APIRouter(
    prefix='/teachers',
    tags=['teachers']
)


@router.get('/current_teacher', response_model=models.Teacher)
def get_teacher(teacher=Depends(get_current_teacher)):
    return teacher


@router.post('/sign-in', response_model=models.Token)
def sign_in(
    auth_data: OAuth2PasswordRequestForm = Depends(),
    teacher_service: TeacherService = Depends()
):
    return teacher_service.auth_teacher(
        auth_data.username,
        auth_data.password,
    )


@router.post('/sign-up', response_model=models.Token)
def add_teacher(new_teacher: models.TeacherBase,
                service: TeacherService = Depends()):
    return service.create(new_teacher)
