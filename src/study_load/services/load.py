from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from src.db import get_session
from ..models import load
from typing import List, Generic, TypeVar, Union
from ..models import links, Teacher, Sgroup, Load

T = TypeVar('T')

class LoadService(Generic[T]):
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def _get(self, id: int, entity: T):
        entity_db:Union[T, None] = self.session.get(entity, id)

        if not entity_db:
            raise HTTPException(status_code=404, detail='Department not found')

        print(entity_db)
        return entity_db


    def _get_entities_by_id(self, ids: List[id], entity: T):
        return list(map(lambda id: self._get(id, entity), ids))

    def get_all(self) -> List[load.Load]:
        result = self.session.execute(select(load.Load))
        loads = result.scalars().all()
        return loads

    def create_load(self, load_data:load.LoadCreate ) -> Load:
       parsed_teachers = self._get_entities_by_id(load_data.teachers, Teacher)
       parsed_sgroups = self._get_entities_by_id(load_data.groups, Sgroup)
       load_db = Load(discipline_id=load_data.discipline_id, teacher=parsed_teachers, sgroup=parsed_sgroups)

       self.session.add(load_db)
       self.session.commit()
       self.session.refresh(load_db)

       return load_db

