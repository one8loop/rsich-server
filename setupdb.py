import sqlite3 as lite
import sys

con = lite.connect('RSI.db')

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS User")
    cur.execute("CREATE TABLE User(Username TEXT UNIQUE, Name TEXT, Surname TEXT, Points INT, Gen_Points INT)")
    cur.execute("INSERT INTO User VALUES('oneloop','Alessandro','Castiglioni',5264,1441)")
    cur.execute("INSERT INTO User VALUES('pdor','Davide','Molinelli',1056,562)")
    cur.execute("INSERT INTO User VALUES('kmer','Emanuele','Falzone',6537,300)")
