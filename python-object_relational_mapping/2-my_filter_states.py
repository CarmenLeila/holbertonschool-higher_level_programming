#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""

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
        "SELECT * FROM states WHERE states.name LIKE BINARY "
        "'{}' ORDER BY states.id".format(sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    myconnect.close()
