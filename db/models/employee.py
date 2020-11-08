from sqlalchemy import Column, String, ForeignKey
from .base import BaseModel


class Employee(BaseModel):
    __tablename__ = 'employees'

    name = Column(String, nullable=False)
    dep_id = Column(ForeignKey("department.id", ondelete='CASCADE'), nullable=False)
