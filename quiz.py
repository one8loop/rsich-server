quiz_la1 = { 'text': 'Dove sono nati i giochi Olimpici?',
             'answers': ['Italia', 'Sudafrica', 'Grecia', 'Spagna'],
             'explanation': 'I primi giochi Olimpici si sono tenuti ad Olimpia nel 776 a.C.',
             'correct': 3 }
quiz_la2 = { 'text': 'Nel ciclismo, di che colore è la maglia del vincitore del Tour de France?',
             'answers': ['Rosa', 'Gialla', 'Verde', 'Bianca'],
             'explanation': 'La scelta della maglia gialla viene fatta risalire al 1913',
             'correct': 2 }
             #frank matana

activeQuizzes = { 'la1': quiz_la1,
                 'la2': quiz_la2 }

def getQuiz(channel):
    for quizChannel in activeQuizzes:
        if quizChannel == channel:
            return activeQuizes[quizChannel]
    return None
