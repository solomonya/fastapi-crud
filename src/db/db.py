from dotenv import dotenv_values
from sqlmodel import create_engine, SQLModel, Session

config = dotenv_values('.env')

DB_URL = config['DB_URL']

engine = create_engine(DB_URL, echo=True)


def get_session():
  session = Session(engine)
  try:
    yield session
  finally:
    session.close()

