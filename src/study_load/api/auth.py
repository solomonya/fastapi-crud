from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.study_load.models import Token
from src.study_load import models
from src.study_load.services import AuthService, get_current_admin

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post('/sign-in', response_model=Token)
def sing_in(
    auth_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends()
):
    return auth_service.authentificate_admin(
        auth_data.username,
        auth_data.password,
    )


@router.post('/sign-up', response_model=Token)
def sign_up(
    admin_data: models.AdminBase,
    auth_service: AuthService = Depends()
):
    return auth_service.register_new_admin(admin_data)


@router.get('/admin/', response_model=models.AdminBase)
def get_admin(admin: models.AdminBase = Depends(get_current_admin)):
    return admin
