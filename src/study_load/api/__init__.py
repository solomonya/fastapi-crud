from fastapi import APIRouter
from .teacher import router as teacher_router

router = APIRouter()

router.include_router(teacher_router)