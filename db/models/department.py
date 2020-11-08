from sqlalchemy import Column, Integer, ForeignKey, String
from .base import BaseModel


class Department(BaseModel):
    __tablename__ = 'department'

    title = Column(String, nullable=False, unique=True)
    parent = Column(ForeignKey("department.id", ondelete='CASCADE'), nullable=True, default=None)
