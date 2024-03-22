#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to MySQL database and list all cities"""

    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL server
    try:
        myconnect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

    # Create cursor object
    cursor = myconnect.cursor()

    # Execute SQL query to select all cities and order by id
    try:
        cursor.execute("SELECT * FROM cities ORDER BY id ASC")
        cities = cursor.fetchall()
    except MySQLdb.Error as e:
        print("Error executing SQL query:", e)
        cursor.close()
        myconnect.close()
        sys.exit(1)

    # Display results
    for city in cities:
        print(city)

    # Close cursor and connection
    cursor.close()
    myconnect.close()
