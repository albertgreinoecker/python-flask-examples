from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) #Die Flask API

#Jede resource muss von der Klasse Resource erben. Alle HTTP-Methoden werden hier auf Python-Methoden abgebildet

class SimpleClass(Resource):
    def get(self):
        return {'param1': 'HELLO',
                'param2' : 13}


#Speichert den Score zu bestimmten Namen
name_score = {}

class SimpleNameScore(Resource):
    def get(self, name):
        if name in name_score:
            return {name: name_score[name]}
        return {"Message" : "Nicht vorhanden"}

    def put(self, name):
        existing = name in name_score
        name_score[name] = request.form['score']
        if existing:
            return {"Message" : "Überschrieben"}
        return {"Message" : "Neu hinzugefügt"}

    def delete(self, name):
        del name_score[name]
        return {"Message": "%s gelöscht" % name}

    def patch(self, name): #Hier das gleiche wie put, weil ja nur ein Attribut (score) vorhanden ist
        name_score[name] = request.form['score']
        return {"Message": "%s gepatched" % name}

#Hier passiert das Mapping auf die Klasse
api.add_resource(SimpleClass, '/')
api.add_resource(SimpleNameScore, '/score/<string:name>')

if __name__ == '__main__':
    app.run(debug=True) #debug=True lädt nach den Änderungen neu


#Aufrufe für SimpleNameScore
# curl http://localhost:5000/score/albert -d "score=100" -X PUT