import sqlite3 as lite

def getQuiz(channel):
    con = lite.connect('RSI.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT rowid, Question FROM Quiz WHERE Network = ? ORDER BY rowid DESC', (channel,))
        row = cur.fetchone()

    if row == None: return None

    return { '_id': row[0], 'id': str(row[0]), 'progam': channel, 'text': row[1] }


def getAnswersForId(id):
    con = lite.connect('RSI.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT A1, A2, A3, A4, CorrectNo FROM Quiz WHERE rowid = ?', (id,))
        row = cur.fetchone()

    if row == None: return None

    response = []
    for num, answer in zip(range(4), row):
        response.append({'_id': num+1, 'id': str(num+1), 'text': answer,
                         'id_question': str(id), 'correct': num+1 == row[4]})

    return response

def getCorrectForId(id):
    con = lite.connect('RSI.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT CorrectNo FROM Quiz WHERE rowid = ?', (id,))
        row = cur.fetchone()

    if row == None: return None

    return row[0]
