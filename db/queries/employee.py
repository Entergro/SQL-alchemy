from db.models import Employee, Department
from ..base import DBSession


def push_new_employee(db: DBSession, e_name: str, e_depart: str = None):
    d_id = db.session.query(Department).filter(Department.title == e_depart).one().id
    new_row = Employee(name=e_name,
                       dep_id=d_id)

    db.session.add(new_row)
    db.session.commit()
