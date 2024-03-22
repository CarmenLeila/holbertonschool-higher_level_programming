#!/usr/bin/python3
""" lists all states with a name starting with N """

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    myconnect = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )

    cursor = database.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    myconnect.close()
