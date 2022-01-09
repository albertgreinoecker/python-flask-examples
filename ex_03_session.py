from flask import Flask, render_template, session

app = Flask(__name__)
#so erzeugt man einen guten secret key:
# python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = '48c1cb4d1388f1504ce904f8b875da9f51f0466d322d3120ec32b0ee14ba40f9'

#Session darf nur innerhalb von den Methoden verwendet werden, sonst fehlt der Kontext!

@app.route('/counter')
def home():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('03_session.html', count=session['counter'])

if __name__ == '__main__':
    app.run(debug=True)