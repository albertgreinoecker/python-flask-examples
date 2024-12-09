from flask import Flask

app = Flask(__name__) # Initialisierung der App
# Hier kommt der code der beim Starten des Servers ausgeführt wird


@app.route('/')
def home():
    return '<b>Hello</b>!!!'  #Dieser Text wird direkt auf der Website angezeigt

@app.route('/htl')
def htl():
    return '<b>Hello</b> HTL!!!'  #Dieser Text wird direkt auf der Website angezeigt

@app.route('/name/<name>')
def name(name):
    return '<b>Hello</b> !!!' + name  #Dieser Text wird direkt auf der Website angezeigt

@app.route('/add/<int:op1>/<int:op2>')
def add(op1, op2):
    return str(op1 + op2)  #Dieser Text wird direkt auf der Website angezeigt

if __name__ == '__main__':
    app.run() #Startet den Server