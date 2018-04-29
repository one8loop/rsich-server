from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
import json, sqlite3 as lite
from quiz import *

app = Flask(__name__)
api = Api(app)

userparser = reqparse.RequestParser()
userparser.add_argument('givePoints', type=int, help='Adds free points to user')

class Quiz(Resource):
    def get(self, channel):
        quiz = getQuiz(channel)
        return quiz


class Leaderboard(Resource):
    def get(self):
        con = lite.connect('RSI.db')
        with con:
            cur = con.cursor()
            cur.execute('SELECT Username, Points, Gen_Points FROM User ORDER BY Gen_Points DESC LIMIT 10')
            rows = cur.fetchall()

        if rows == None:
            abort(400, message='No user found')

        leaderboard = []
        for user in rows:
            leaderboard.append({ 'username': user[0], 'points': user[1], 'general_points': user[2] })
        return leaderboard


class User(Resource):
    def get(self, userId):
        con = lite.connect('RSI.db')
        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM User WHERE rowid = ?', userId)
            row = cur.fetchone()

        if row == None:
            abort(400, message='User not found')

        user = { 'username': row[0],
                 'name': row[1],
                 'surname': row[2],
                 'points': row[3],
                 'general_points': row[4] }

        return user

    def put(self, userId):
        args = userparser.parse_args()
        if args['givePoints'] == 1:
            con = lite.connect('RSI.db')
            with con:
                cur = con.cursor()
                cur.execute('UPDATE User SET Points = Points + 50, Gen_Points = Gen_Points + 50 WHERE rowid = ?', userId)
        return 'Accepted', 202


api.add_resource(Quiz, '/quiz/<string:channel>')
api.add_resource(Leaderboard, '/leaderboard')
api.add_resource(User, '/user/<string:userId>')

if __name__ == '__main__':
#    app.run(debug=False)
    app.run(host='0.0.0.0', port=5689, debug=False) # To open to the network
