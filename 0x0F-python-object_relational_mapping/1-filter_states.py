#!/usr/bin/python3
""" script that lists all states with a name starting with upper N """
import MySQLdb
import sys


if __name__ == "__main__":
    _args = sys.argv
    _user = _args[1]
    _passwd = _args[2]
    _db = _args[3]

    data_base = MySQLdb.connect("localhost",
                                _user,
                                _passwd,
                                _db,
                                3306)
    cur = data_base.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY
    states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    data_base.close()
