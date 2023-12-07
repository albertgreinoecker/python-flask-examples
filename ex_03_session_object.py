from flask import Flask, render_template, session, jsonify
from flask_session import Session  # new style
'''
Möchte man z.B.: Objekte in der Session speichern, gibt es bei der normalen Verwendung ein Problem, 
weil Flask die Session Info als JSON-String (verschlüsselt!) in einem Cookie speichert. 

Es gäbe die Möglichkeit, das Schreiben als JSON selbst zu implementieren bzw. das Objekt o mit o.__dict__ in ein Dictionary
zu übertragen, aber die hier verwendete Erweiterung flask-session macht es einfacher. Hier werden die Session-Daten im Dateisystem des Servers gespeichert.

pip3 install flask_session
'''
app = Flask(__name__)

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
#Session darf nur innerhalb von den Methoden verwendet werden, sonst fehlt der Kontext!


class Question:
    def __init__(self, text, level, answers, correct):
        self.text = text
        self.level  = level
        self.answers = answers
        self.correct = correct

@app.route('/question')
@app.route('/question/<int:correct>')
def question(correct = 0):
    feedback = ''
    if 'question' in session:
        if session['question'].correct == correct:
            feedback = 'correct!'
        else:
            feedback = 'wrong'
        session['question'] =  Question('Q2', 1, ['E','F','G','H'], 1)
    else: # Neue Session zum Starten
        session['question'] = Question('Q1', 0, ['A','B','C','D'], 3)
    return render_template('03_session_object.html', feedback=feedback, question= session['question'])

if __name__ == '__main__':
    app.run(debug=True, port=5001)