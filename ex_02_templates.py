from flask import Flask, render_template # Zusätzlicher Import für's rendern

app = Flask(__name__)

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

@app.route('/temp')
def home():
    q = Question('What is the capital of Austria?', 'Vienna')
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAI', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    dict = {'MON' : 'work', 'TUE' : 'work', 'WED' : 'work', 'THU' : 'work', 'FRI' : 'depends', 'SAT' : 'weekend', 'SUN' :'weekend' }
    return render_template('02_templates.html', name='jinja2', months=months, dict=dict, question=q)



if __name__ == '__main__':
    app.run(debug=True)