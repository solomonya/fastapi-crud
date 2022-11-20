from fastapi import Depends, HTTPException
from src.db import get_session
from sqlmodel import Session, select
from ..models import Sgroup, StudyGroupBase
from typing import List

class StudyGroupService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def _get(self, study_group_id: int) -> Sgroup:
        study_group = self.session.get(Sgroup, study_group_id)
        if not study_group:
            raise HTTPException(status_code=404, detail='Study group not found')

        return study_group

    def get_all(self) -> List[Sgroup]:
       groups = self.session.exec(select(Sgroup)).all()
       return groups

    def create(self, data: StudyGroupBase) -> Sgroup:
      study_group = Sgroup(**data.dict())
      self.session.add(study_group)
      self.session.commit()
      self.session.refresh(study_group)

      return study_group

    def update(self, data: Sgroup) -> Sgroup:
       study_group_db = self._get(data.id)
       study_grpup_data = data.dict(exclude_unset=True)

       for field, value in study_grpup_data.items():
           setattr(study_group_db, field, value)

       self.session.add(study_group_db)
       self.session.commit()
       self.session.refresh(study_group_db)

       return self._get(data.id)
 
    def delete(self, study_group_id: int) -> dict[str, bool]:
        study_group_db = self._get(study_group_id)
        self.session.delete(study_group_db)
        self.session.commit()

        return { "ok": True }
