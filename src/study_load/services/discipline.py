from src.db import get_session
from fastapi import Depends, HTTPException
from sqlmodel import Session, select


from ..models import Discipline
from typing import List


class DisciplineService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, discipline_id: int) -> Discipline:
        discipline = self.session.get(Discipline, discipline_id)

        if not discipline:
            raise HTTPException(status_code=404, detail='Department not found')

        return discipline

    def get_one(self, id: int) -> Discipline:
        return self._get(id)

    def get_all(self) -> List[Discipline]:
        result = self.session.execute(select(Discipline))
        disciplines = result.scalars().all()
        return disciplines

    def create_discipline(self, discipline_data) -> Discipline:
        discipline = Discipline(**discipline_data.dict())
        self.session.add(discipline)
        self.session.commit()
        self.session.refresh(discipline)

        return discipline

    def update_discipline(self, discipline: Discipline) -> Discipline:
        discipline_db = self._get(discipline.id)
        discipline_data = discipline.dict(exclude_unset=True)

        for field, value in discipline_data.items():
            setattr(discipline_db, field, value)

        self.session.add(discipline_db)
        self.session.commit()
        self.session.refresh(discipline_db)

        return discipline_db

    def delete_discipline(self, discipline_id: int) -> dict[str, bool]:
        discipline_db = self._get(discipline_id)
        self.session.delete(discipline_db)
        self.session.commit()

        return {"success": True}
