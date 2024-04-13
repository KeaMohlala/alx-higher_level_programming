#!/usr/bin/python3
"""
module of a script that list all cities from the database
"""
import MySQLdb
import sys


def main(user, password, db_name):
    """
    function that carries out the purpose of the script i.e
    listing all cities from database 'hbtn_0e_4_usa'

    Args: username, password, database name
    """
    conn = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )

    cursor = conn.cursor()

    query = """
        SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    user, password, db_name = sys.argv[1:]
    main(user, password, db_name)
