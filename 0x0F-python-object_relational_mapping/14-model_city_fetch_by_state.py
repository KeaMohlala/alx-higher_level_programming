#!/usr/bin/python3
"""
Script that lists all City objects from database 'hbtn_0e_14_usa'.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


def main(user, password, db_name):
    """
    function that carries out the purpose of the script i.e
    listing all cities from the database 'hbtn_0e_14_usa'

    Args: username, password and the database name
    """
    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name, City.id, City.name)\
        .order_by(City.id)\
        .join(City)\
        .filter(State.id == City.state_id)\
        .all()

    for city in cities:
        print(f"{city[0]}: ({city[1]}) {city[2]}")

    session.close()


if __name__ == "__main__":
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    main(user, password, db_name)
