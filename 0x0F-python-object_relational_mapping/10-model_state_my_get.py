#!/usr/bin/python3
"""
Script that prints the State objects with the name passed as argument
from database 'hbtn_0e_6_usa'.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(user, password, db_name, state_name):
    """
    function that carries out the purpose of the script i.e
    listing the first state from the database 'hbtn_0e_6_usa'
    where the name matches the argument

    Args: username, password, database, state name
    """
    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == state_name).first()

    if states:
        print(f"{states.id}")
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    user, password, db_name, state_name = sys.argv[1:]
    main(user, password, db_name, state_name)
