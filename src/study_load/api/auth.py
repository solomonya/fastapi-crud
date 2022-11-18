from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.study_load.models import Token

router = APIRouter(
  prefix='/auth',
  tags=['auth']
)

@router.post('/sign-in', response_model=Token)
def sing_in(auth_data: OAuth2PasswordRequestForm = Depends()):
  pass