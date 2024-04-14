#!/usr/bin/python3
"""
Script that adds the State object "Louisiana"
to database 'hbtn_0e_6_usa'.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def state_new(user, password, db_name, state_name):
    """
    function that carries out the purpose of the script i.e
    adds object 'Louisiana' to the database 'hbtn_0e_6_usa'

    Args: username, password and the database name
    """
    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name=state_name)
    session.add(new_state)
    session.commit()

    print(f"{new_state.id}")

    session.close()


if __name__ == "__main__":
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    state_new(user, password, db_name, "Louisiana")
