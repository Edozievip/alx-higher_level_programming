#!/usr/bin/python3
"""
This lists all the states from the database
It takes 3 arguements: mysql username, msql password, database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
