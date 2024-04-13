#!/usr/bin/python3
"""
module of a script that list all cities of the state
using thats name of the state as an argument
"""
import MySQLdb
import sys


def main(user, password, db_name, state_name):
    """
    function that carries out the purpose of the script i.e
    listing all cities from a specified from database 'hbtn_0e_4_usa'

    Args: username, password, database name, state_name
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
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row[0])

    conn.close()


if __name__ == "__main__":
    user, password, db_name, state_name = sys.argv[1:]
    main(user, password, db_name, state_name)
