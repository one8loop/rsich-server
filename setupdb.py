import sqlite3 as lite
import random as rnd
import sys

users = [ ['oneloop','Alessandro','Castiglioni',0,0],
          ['pdor','Davide','Molinelli',0,0],
          ['kmer','Emanuele','Falzone',0,0],
          ['assionito','Name','Surname',0,0],
          ['crossie','Name','Surname',0,0],
          ['latchip','Name','Surname',0,0],
          ['cormin','Name','Surname',0,0],
          ['lettwarz','Name','Surname',0,0],
          ['saluatom','Name','Surname',0,0],
          ['travere','Name','Surname',0,0],
          ['dakertile','Name','Surname',0,0],
          ['itscool','Name','Surname',0,0],
          ['schoolnei','Name','Surname',0,0] ]

quizzes = [ ['la1',
             'Dove sono nati i giochi Olimpici?',
             'Italia', 'Sudafrica', 'Grecia', 'Spagna', 3],
             ['la2',
              'Nel ciclismo, di che colore è la maglia del vincitore del Tour de France?',
              'Rosa', 'Gialla', 'Verde', 'Bianca', 2
             ] ]

polls = [ ['Il surriscaldamento globale rappresenta un problema immediato per la Svizzera?',
           'Sì', 'No'] ]

for user in users:
    user[3] = rnd.randint(0, 5000)
    user[4] = rnd.randint(0, 1500)


con = lite.connect('RSI.db')

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS User")
    cur.execute("CREATE TABLE User(Username TEXT UNIQUE, Name TEXT, Surname TEXT, Points INT, Gen_Points INT)")
    cur.executemany("INSERT INTO User VALUES(?, ?, ?, ?, ?)", users)

    cur.execute("DROP TABLE IF EXISTS Quiz")
    cur.execute("CREATE TABLE Quiz(Network TEXT, Question TEXT, A1 TEXT, A2 TEXT, A3 TEXT, A4 TEXT, CorrectNo INT)")
    cur.executemany("INSERT INTO Quiz VALUES(?, ?, ?, ?, ?, ?, ?)", quizzes)

    cur.execute("DROP TABLE IF EXISTS Poll")
    cur.execute("CREATE TABLE Poll(Question TEXT, A1 TEXT, A2 TEXT, CountA1 INT, CountA2 INT)")
    cur.executemany("INSERT INTO Poll VALUES(?, ?, ?, 0, 0)", polls)
