from sqlmodel import Session, select
from fastapi import Depends, HTTPException, status
from src.db import get_session
from typing import List
from src.study_load.models import Teacher
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.hash import bcrypt
import dotenv
from datetime import datetime, timedelta

from pydantic import ValidationError

from src.study_load import models


config = dotenv.dotenv_values('.env')

jwt_secret = config['JWT_SECRET']
jwt_algorithm = config['JWT_ALGORITHM']
jwt_expires_s = config['JWT_EXPIRES_S']


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/teachers/sign-in/')


def get_current_teacher(token: str = Depends(oauth2_scheme)) -> models.TeacherBase:
    return TeacherService.verify_token(token)


class TeacherService:
    @classmethod
    def verify_token(cls, token: str) -> models.Teacher:
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

        teacher_data = payload.get('teacher')

        try:
            teacher = models.Teacher.parse_obj(teacher_data)
        except ValidationError:
            raise exception from None

        return teacher

    @classmethod
    def create_token(cls, teacher: models.Teacher) -> models.Token:
        teacher_data = models.Teacher.from_orm(teacher)
        for field, value in teacher_data.dict().items():
            setattr(teacher_data, field, str(value))

        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=int(jwt_expires_s)),
            'sub': str(teacher_data.id),
            'teacher': teacher_data.dict(),
        }

        token = jwt.encode(
            payload,
            jwt_secret,
            algorithm=jwt_algorithm
        )

        return models.Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, id: int) -> Teacher:
        teacher = self.session.get(Teacher, id)
        if not teacher:
            raise HTTPException(status_code=404, detail='Teacher not found')

        return teacher

    def get_one(self, id: int) -> Teacher:
        return self._get(id)

    def get_all(self) -> List[Teacher]:
        result = self.session.execute(select(Teacher))
        teachers = result.scalars().all()
        return teachers

    def create(self, new_teacher: models.TeacherBase) -> models.Token:
        teacher = Teacher(
            **new_teacher.dict()
        )

        self.session.add(teacher)
        self.session.commit()
        self.session.refresh(teacher)

        return self.create_token(teacher)

    def auth_teacher(self, email: str, password: str) -> models.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        teacher = (
            self.session
            .exec(
                select(models.Teacher)
                .where(models.Teacher.email == email)
            )
        ).first()

        if not teacher:
            raise exception

        if not password == teacher.password_hash:
            raise exception

        return self.create_token(teacher)
