# Declarative-Variante wird hier benutzt
from flask import Flask, request,jsonify
from sqlalchemy import Column, Integer, Text, Float, DateTime, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
from flask_restful import Resource, Api
from dataclasses import dataclass

Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen
metadata = Base.metadata

engine = create_engine('sqlite:////home/albert/tmp/geoinfo.sqlite3') #Welche Datenbank wird verwendet
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine))
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
        return {"Message": "Stored"}

    def put(self, id):
        data = request.form['info']
        print(data)
        info = GeoInfo(long=12, lat=14, message='aaa')
        db_session.add(info)
        db_session.flush()
        return jsonify(info)

class GeoInfosRESTs(Resource):
    def get(self):
        infos = GeoInfo.query.all()
        print(infos)
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


