#!/usr/bin/python3
"""
module of a script that list all states starting with 'N' from the database
"""
import MySQLdb
import sys


def main(user, password, db_name):
    """
    function that carries out the purpose of the script i.e
    listing all states starting with N from the database 'hbtn_0e_0_usa'

    Args: username, password and the database name
    """
    conn = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )

    cursor = conn.cursor()
    cursor.execute(
            """
            SELECT * FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER by id ASC;
            """
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    main(user, password, db_name)
