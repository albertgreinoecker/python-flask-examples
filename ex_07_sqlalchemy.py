# Declarative-Variante wird hier benutzt
from flask import Flask, jsonify, render_template
from sqlalchemy import Column, Integer, Text
from sqlalchemy import create_engine,  or_
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func

Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen
metadata = Base.metadata

engine = create_engine('sqlite:///data/millionaire.sqlite3')
db_session = scoped_session(sessionmaker(autoflush=True, bind=engine))
Base.query = db_session.query_property() #Dadurch hat jedes Base - Objekt (also auch ein Millionaire) ein Attribut query für Abfragen
app = Flask(__name__) #Die Flask-Anwendung

class Millionaire(Base):
    __tablename__ = 'millionaire'  # Abbildung auf diese Tabelle

    id = Column(Integer, primary_key=True)
    difficulty = Column(Integer)
    question = Column(Text)
    correct_answer = Column(Text)
    answer2 = Column(Text)
    answer3 = Column(Text)
    answer4 = Column(Text)
    background_information = Column(Text)

    def serialize(self):
        return {'id' : self.id,
                'difficulty':  self.difficulty,
                'question' : self.question}
@app.route('/')
def home():
    m = Millionaire.query.filter(Millionaire.difficulty == 1).order_by(func.random()).first()
    print(m.question)
    return m.question

@app.route('/search/<string:needle>')
def search(needle):
    #or_ nicht vergessen zu importieren
    res = Millionaire.query.filter(or_(Millionaire.question.contains(needle), Millionaire.correct_answer.contains(needle))) #kommt in einem der beiden Spalten ein bestimmter String vor
    resA = []
    for m in res:
        print (type(m), m.serialize())
        resA.append(m.serialize())
    return jsonify(resA) #Schreibe das Ergebnis als


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


