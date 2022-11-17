from fastapi import APIRouter
from .teacher import router as teacher_router
from .department import router as department_router

router = APIRouter()

routes  = (
  [
    teacher_router,
    department_router
  ]
)

for entity in routes:
  router.include_router(entity)