# Declarative-Variante wird hier benutzt
from flask import Flask, request,jsonify
from sqlalchemy import Column, Integer, Text, Float, DateTime, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
from flask_restful import Resource, Api
from dataclasses import dataclass
import json

Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen
metadata = Base.metadata

engine = create_engine('sqlite:////home/albert/tmp/geoinfo.sqlite3') #Welche Datenbank wird verwendet
db_session = scoped_session(sessionmaker(autoflush=True, bind=engine))
Base.query = db_session.query_property() #Dadurch hat jedes Base - Objekt (also auch ein GeoInfo) ein Attribut query für Abfragen
app = Flask(__name__) #Die Flask-Anwendung
api = Api(app) #Die Flask API

@dataclass #Diese ermoeglicht das Schreiben als JSON mit jsonify
class GeoInfo(Base):
    __tablename__ = 'geoinfo'  # Abbildung auf diese Tabelle
    #Deklaration mit welchen Typen die einzelnen Attribute als JSON geschrieben werden sollen
    id: int
    name: str
    long: float
    lat : float
    message: str
    when: str

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    long = Column(Float)
    lat = Column(Float)
    message = Column(Text)
    when = Column(DateTime, default=func.now())

class GeoInfoREST(Resource):
    def get(self, id):
        info = GeoInfo.query.get(id)
        return jsonify(info)
    def put(self, id):
        data = request.get_json(force=True)['info']
        print(data)
        info = GeoInfo(name=data['name'], long=data['long'], lat=data['lat'], message=data['message'])
        db_session.add(info)
        db_session.flush()
        db_session.commit()
        return jsonify(info)
    def delete(self,id):
        info = GeoInfo.query.get(id)
        if info is None:
            return jsonify({'message': 'object with id %d does not exist' % id})
        db_session.delete(info)
        db_session.flush()
        return jsonify({'message': '%d deleted' % id})

    def patch(self, id):
        info = GeoInfo.query.get(id)
        if info is None:
            return jsonify({'message': 'object with id %d does not exist' % id})
        data = json.loads(request.json['info'])
        if 'name' in data:
            info.name = data['name']
        if 'long' in data:
            info.long = data['long']
        if 'lat' in data:
            info.lat = data['lat']
        if 'message' in data:
            info.message = data['message']
        db_session.add(info)
        db_session.flush()
        return jsonify({'message': 'object with id %d modified' % id})

class GeoInfosRESTs(Resource):
    def get(self):
        infos = GeoInfo.query.all()
        return jsonify(infos)


api.add_resource(GeoInfoREST, '/geoinfo/<int:id>')
api.add_resource(GeoInfosRESTs, '/geoinfos/')

@app.teardown_appcontext
def shutdown_session(exception=None):
    print("Shutdown Session")
    db_session.remove()

def init_db():
    # Erzeugen der Tabellen für die Klassen, die oben deklariert sind (muss nicht sein, wenn diese schon existiert)
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)


