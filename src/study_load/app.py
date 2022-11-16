from fastapi import FastAPI, Depends
from src.db.db import init_db, get_session
from src.study_load.models.teacher import Teacher
from sqlmodel import Session

app = FastAPI()

@app.get('/')
def root():
  return {'message': 'Hello, world!'}

@app.post('/teachers')
def add_teacher(teacher: Teacher, session: Session = Depends(get_session)):
  teacher = Teacher(
    name=teacher.name,
    academic_degree=teacher.academic_degree,
    position=teacher.position
  )
  session.add(teacher)
  session.commit()
  session.refresh(teacher)
  return teacher