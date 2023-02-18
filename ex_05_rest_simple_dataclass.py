from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from dataclasses import dataclass

app = Flask(__name__)
api = Api(app) #Die Flask API

'''
Für die Serialisierung werden die Werte name, age verwendet, comment nicht
'''
@dataclass
class Person:
    id: int
    name : str
    age : int

    def __init__(self, id, name, age, comment):
        self.id = id
        self.name = name
        self.age  = age
        self.comment = comment


persons = {0 : Person(0, "Hubert", 30, "comment 1"),
           1 : Person(1, "Herbert", 40, "comment 2")}


class PersonService(Resource):
    def get(self, id):
        print("get")
        print(persons)
        if id in persons:
            return jsonify(persons[id])
        return {"Message" : "%s not found" % id}

    def put(self, id):
        data = request.get_json(force=True)
        persons[id] = Person(data['id'], data['name'], data['age'], data['comment'])
        print("put")
        print(persons)
        return {"Message": "%s gespeichert" % id}

    def delete(self, id):
        del persons[id]
        return {"Message": "%s gelöscht" % id}

    def patch(self, id):
        data = request.get_json(force=True)
        print('patch')
        if 'comment' in data:
            print('comment')
            persons[id].comment = data['comment']
        if 'age' in data:
            persons[id].age = data['age']
        if 'name' in data:
            persons[id].name = data['name']
        return {"Message": "%d gepatched" % id}

#Hier passiert das Mapping auf die Klasse
api.add_resource(PersonService, '/person/<int:id>')

if __name__ == '__main__':
    app.run(debug=True) #debug=True lädt nach den Änderungen neu

