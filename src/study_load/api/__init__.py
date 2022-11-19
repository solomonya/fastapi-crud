from fastapi import APIRouter
from .teacher import router as teacher_router
from .department import router as department_router
from .auth import router as auth_router
from .speciality import router as speciality_router

router = APIRouter()

routes  = (
  [
    teacher_router,
    department_router,
    auth_router,
    speciality_router
  ]
)

for entity in routes:
  router.include_router(entity)