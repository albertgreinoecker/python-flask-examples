from flask import Flask

app = Flask(__name__) # Initialisierung der App
# Hier kommt der code der beim Starten des Servers ausgeführt wird


@app.route('/')
def home():
    return 'Hello!!!'  #Dieser Text wird direkt auf der Website angezeigt

if __name__ == '__main__':
    app.run() #Startet den Server