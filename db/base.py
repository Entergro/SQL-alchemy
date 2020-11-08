from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class DBSession(object):
    __db = 'sqlite:///project.db?check_same_thread=False'
    session = None

    def __init__(self):
        engine = create_engine(self.__db)
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine)
        self.session = session_factory()
