from fastapi import APIRouter
from .teacher import router as teacher_router
from .department import router as department_router
from .auth import router as auth_router
from .speciality import router as speciality_router
from .study_group import router as study_group_router
from .student import router as students_router
from .discipline import router as discipline_router
from .load import router as load_router

router = APIRouter()

routes  = (
  [
    teacher_router,
    department_router,
    auth_router,
    speciality_router,
    study_group_router,
    students_router,
    discipline_router,
    load_router,
  ]
)

for entity in routes:
  router.include_router(entity)
