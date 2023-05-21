# Declarative-Variante wird hier benutzt
from flask import Flask, jsonify, render_template
from sqlalchemy import Column, Integer, String, create_engine,  or_, ForeignKey, Table, select
from sqlalchemy.orm import scoped_session, sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.sql.expression import func
from dataclasses import dataclass

Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen
metadata = Base.metadata

engine = create_engine('sqlite:///data/uni.sqlite',  echo=True)
db_session = scoped_session(sessionmaker(autoflush=True, bind=engine))
Base.query = db_session.query_property() #Dadurch hat jedes Base - Objekt (also auch ein Millionaire) ein Attribut query für Abfragen
app = Flask(__name__) #Die Flask-Anwendung

@dataclass
class Assistenten(Base):
    __tablename__ = 'Assistenten'
    PerslNr:int
    Name:str
    Fachgebiet:str
    professor_boss: object

    PerslNr = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False)
    Fachgebiet = Column(String(100), nullable=False)
    Boss = Column(Integer, ForeignKey('Professoren.PersNr'), nullable=False)
    professor_boss = relationship("Professoren", back_populates="assistenten")
@dataclass
class Professoren(Base):
    __tablename__ = 'Professoren'

    PersNr:int
    Name : str
    Rang: str
    Raum: str
    vorlesungen: object

    PersNr = Column(Integer, primary_key=True)
    Name = Column(String(100))
    Rang = Column(String(100))
    Raum = Column(String(100))
    vorlesungen = relationship("Vorlesungen", back_populates="professor")
    assistenten =  relationship("Assistenten", back_populates="professor_boss")

hoeren = Table('hoeren',
    Base.metadata,
    Column('MatrNr', Integer, ForeignKey('Studenten.MatrNr')),
    Column('VorlNr', Integer, ForeignKey('Vorlesungen.VorlNr'))
    )

@dataclass
class Studenten(Base):
    __tablename__ = 'Studenten'

    MatrNr : int
    Name : str
    Semester : int
    #vorlesungen :object

    MatrNr = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False)
    Semester = Column(Integer, nullable=False)
    #vorlesungen = relationship('Vorlesungen', secondary=hoeren, backref='studenten')

@dataclass
class Vorlesungen(Base):
    __tablename__ = 'Vorlesungen'

    VorlNr:int
    Titel:str
    SWS:int
    #professor: object
    studenten: object

    VorlNr = Column(Integer, primary_key=True)
    Titel = Column(String(100), nullable=False)
    SWS = Column(Integer, nullable=False)
    gelesen_von = Column(Integer, ForeignKey('Professoren.PersNr'), nullable=False)
    professor = relationship("Professoren", back_populates="vorlesungen")
    studenten = relationship('Studenten', secondary=hoeren, backref='vorlesungen')


@app.route('/')
def home():
    s = Studenten.query.all()
    print(s)
    return jsonify(s)

@app.route('/assistenten')
def assistenten():
    res = Assistenten.query.all()
    return jsonify(res)



@app.route('/professoren')
def professoren():
    res = Professoren.query.all()
    return jsonify(res)


@app.route('/vorlesungen')
def vorlesungen():
    res = Vorlesungen.query.all()
    for r in res:
        print(r.professor.Name)
    return jsonify(res)


@app.route('/studenten')
def studenten():
    res = Studenten.query.all()
    # for r in res:
    #     print(r.professor.Name)
    return jsonify(res)

@app.route('/queries')
def queries():
    res = Studenten.query.order_by(Studenten.Name).limit(3).all(); #sortiere nach dem Namen und hole die ersten 3
    for r in res:
        print(r.Name)


    # See Examples : https://docs.sqlalchemy.org/en/14/orm/quickstart.html#simple-select
    # and: https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    stmt = select(Studenten).where(Studenten.Semester >= 12)
    res = []
    for x in db_session.scalars(stmt):
        res.append({'Name' : x.Name, 'Semester' : x.Semester})

    return jsonify(res)



@app.teardown_appcontext
def shutdown_session(exception=None):
    print("Shutdown Session")
    db_session.remove()

def init_db():
    # Erzeugen der Tabellen für die Klassen, die oben deklariert sind (muss nicht sein, wenn diese schon existiert)
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5001)


