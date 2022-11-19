import dotenv
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.hash import bcrypt

from sqlmodel import Session, select
from pydantic import ValidationError

from src.study_load import models

from src.db import get_session

config = dotenv.dotenv_values('.env')

jwt_secret = config['JWT_SECRET']
jwt_algorithm = config['JWT_ALGORITHM']
jwt_expires_s = config['JWT_EXPIRES_S']


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in/')

def get_current_admin(token: str = Depends(oauth2_scheme)) -> models.AdminBase:
  return AuthService.verify_token(token)

class AuthService:
  @classmethod
  def verify_password(cls, plain_pass: str, hashed_pass: str) -> bool:
    return bcrypt.verify(plain_pass, hashed_pass)

  @classmethod
  def hash_pass(cls, plain_pass: str) -> str:
    return bcrypt.hash(plain_pass)

  @classmethod
  def verify_token(cls, token: str) -> models.AdminBase:
    exception = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail='Could not validate credentials',
      headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
      payload = jwt.decode(
        token,
        jwt_secret,
        algorithms=[jwt_algorithm]
      )
    except JWTError:
      raise exception from None

    admin_data = payload.get('admin')

    try:
      admin = models.Admin.parse_obj(admin_data)
    except ValidationError:
      raise exception from None

    return admin

  @classmethod
  def create_token(cls, admin: models.Admin) -> models.Token:
    admin_data = models.Admin.from_orm(admin)
    now = datetime.utcnow()
    payload = {
      'iat': now,
      'nbf': now,
      'exp': now + timedelta(seconds=int(jwt_expires_s)),
      'sub': str(admin_data.id),
      'admin': admin_data.dict(),
    }

    token = jwt.encode(
      payload,
      jwt_secret,
      algorithm=jwt_algorithm
    )

    return models.Token(access_token=token)

  def __init__(self, session: Session = Depends(get_session)):
    self.session = session

  def register_new_admin(self, admin_data: models.AdminBase) -> models.Token:
    admin = models.Admin(
      email=admin_data.email,
      password_hash=self.hash_pass(admin_data.password_hash)
    )

    self.session.add(admin)
    self.session.commit()
    return self.create_token(admin)


  def authentificate_admin(self, email: str, password: str) -> models.Token:
    exception = HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail='Incorrect username or password',
          headers={'WWW-Authenticate': 'Bearer'},
        )

    admin = (
      self.session
      .execute(
        select(models.Admin)
        .where(models.Admin.email == email)
        )
    ).scalars().first()

    if not admin:
      raise exception

    if not self.verify_password(password, admin.password_hash):
      raise exception

    return self.create_token(admin)
