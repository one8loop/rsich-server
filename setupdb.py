import sqlite3 as lite
import random as rnd
import sys

con = lite.connect('RSI.db')

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS User")
    cur.execute("CREATE TABLE User(Username TEXT UNIQUE, Name TEXT, Surname TEXT, Points INT, Gen_Points INT)")
    cur.execute("INSERT INTO User VALUES('oneloop','Alessandro','Castiglioni',5264,1441)")
    cur.execute("INSERT INTO User VALUES('pdor','Davide','Molinelli',1056,562)")
    cur.execute("INSERT INTO User VALUES('kmer','Emanuele','Falzone',6537,300)")
    cur.execute("INSERT INTO User VALUES('assionito','Name','Surname',?,?)",(rnd.randint(0, 5000),rnd.randint(0, 1500)))
    cur.execute("INSERT INTO User VALUES('crossie','Name','Surname',?,?)",(rnd.randint(0, 5000),rnd.randint(0, 1500)))
    cur.execute("INSERT INTO User VALUES('latchip','Name','Surname',?,?)",(rnd.randint(0, 5000),rnd.randint(0, 1500)))
    cur.execute("INSERT INTO User VALUES('cormin','Name','Surname',?,?)",(rnd.randint(0, 5000),rnd.randint(0, 1500)))
    cur.execute("INSERT INTO User VALUES('lettwarz','Name','Surname',?,?)",(rnd.randint(0, 5000),rnd.randint(0, 1500)))
    cur.execute("INSERT INTO User VALUES('saluatom','Name','Surname',?,?)",(rnd.randint(0, 5000),rnd.randint(0, 1500)))
    cur.execute("INSERT INTO User VALUES('travere','Name','Surname',?,?)",(rnd.randint(0, 5000),rnd.randint(0, 1500)))
    cur.execute("INSERT INTO User VALUES('dakertile','Name','Surname',?,?)",(rnd.randint(0, 5000),rnd.randint(0, 1500)))
    cur.execute("INSERT INTO User VALUES('itscool','Name','Surname',?,?)",(rnd.randint(0, 5000),rnd.randint(0, 1500)))
    cur.execute("INSERT INTO User VALUES('schoolnei','Name','Surname',?,?)",(rnd.randint(0, 5000),rnd.randint(0, 1500)))
