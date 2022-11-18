from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.hash import bcrypt

from sqlmodel import Session

from src.study_load import models

from src.db import get_session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in/')