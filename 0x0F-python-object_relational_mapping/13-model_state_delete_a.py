#!/usr/bin/python3
"""
Script that deletes State objects containing
the letter a from database 'hbtn_0e_6_usa'.
"""
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(user, password, db_name):
    """
    function that carries out the purpose of the script i.e
    deletes states with the letter 'a' from the database 'hbtn_0e_6_usa'

    Args: username, password and the database name
    """
    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State)\
        .filter(State.name.like('%a%'))\
        .delete(synchronize_session=False)
    session.commit()

    session.close()


if __name__ == "__main__":
    user, password, db_name = sys.argv[1:]
    main(user, password, db_name)
