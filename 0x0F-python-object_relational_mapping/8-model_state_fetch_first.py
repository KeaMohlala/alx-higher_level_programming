#!/usr/bin/python3
"""
Script that lists the State objects from database 'hbtn_0e_6_usa'.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(user, password, db_name):
    """
    function that carries out the purpose of the script i.e
    listing the first state from the database 'hbtn_0e_6_usa'

    Args: username, password and the database name
    """
    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()

    if states:
        print(f"{states.id}: {states.name}")
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    main(user, password, db_name)
