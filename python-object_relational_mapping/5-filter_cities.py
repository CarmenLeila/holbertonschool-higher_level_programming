#!/usr/bin/python3
""" script that lists all cities of a state """

import MySQLdb
import sys
import os

username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
database = os.getenv('DB_NAME')


if __name__ == "__main__":
    myconnect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = myconnect.cursor()
    cmd = ("SELECT cities.name FROM cities "
           "INNER JOIN states ON cities.state_id = states.id "
           "WHERE states.name = %s ORDER BY cities.id")
    cursor.execute(cmd, (sys.argv[4],))

    rows = cursor.fetchall()
    to_string = ', '.join(map(" ".join, rows))
    print(to_string)

    myconnect.close()
