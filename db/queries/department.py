from db.models import Department
from ..base import DBSession


def get_depart_id_by_name(db: DBSession, d_title: str) -> int:
    depart = db.session.query(Department).filter(Department.title == d_title).one()

    return depart.id


def push_new_depart(db: DBSession, d_title: str, d_parent: str = None):
    d_id = db.session.query(Department).filter(Department.title == d_parent).one().id if d_parent else None
    new_row = Department(title=d_title,
                         parent=d_id)

    db.session.add(new_row)
    db.session.commit()
