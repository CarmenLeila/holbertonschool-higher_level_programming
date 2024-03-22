#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    """including the guard clause"""

    """connection to the MySQLdb database"""
    myconnect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])

    cursor = myconnect.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN"
        "states ON cities.state_id = states.id ORDER BY cities.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    myconnect.close()
