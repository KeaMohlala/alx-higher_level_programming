#!/usr/bin/python3
"""
module of a script that list all states from the database
where the name matches the provided argument
"""
import MySQLdb
import sys


def main(user, password, db_name, state_name):
    """
    function that carries out the purpose of the script i.e
    listing all states from database 'hbtn_0e_0_usa'
    where the name matches the argument

    Args: username, password, database name and state name to search
    """
    conn = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )

    cursor = conn.cursor()

    # prepare the SQL query with the user input
    query = """
        SELECT * FROM states
        WHERE name LIKE BINARY %s
        ORDER BY id ASC;
    """

    # execute the query with the state name as a parameter
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    user, password, db_name, state_name = sys.argv[1:]
    main(user, password, db_name, state_name)
