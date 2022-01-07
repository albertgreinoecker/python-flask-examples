from flask import Flask, render_template # Zusätzlicher Import für's rendern

app = Flask(__name__)

@app.route('/temp')
def home():
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAI', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    dict = {'MON' : 'work', 'TUE' : 'work', 'WED' : 'work', 'THU' : 'work', 'FRI' : 'depends', 'SAT' : 'weekend', 'SUN' :'weekend' }
    return render_template('02_templates.html', name='jinja2', months=months, dict=dict)

if __name__ == '__main__':
    app.run(debug=True)