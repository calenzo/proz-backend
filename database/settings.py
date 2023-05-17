from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = f"sqlite:///prozbackend.sql"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class ConnectionDatabase:
    def __init__(self):
        self.session = Session()


def create_tables():
    Base.metadata.create_all(bind=engine)
