from sqlalchemy import Column, Integer, Date
from ..base import Base

from datetime import datetime


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(Date, default=datetime.now())
    updated_at = Column(Date, default=datetime.now(), onupdate=datetime.now())
