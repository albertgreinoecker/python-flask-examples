# Declarative-Variante wird hier benutzt
from sqlalchemy import Column, Integer, Text, Sequence
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func

Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen


engine = create_engine('sqlite:////home/albert/tmp/person.sqlite3')
db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=engine)) #Es ginge auch einfacher, aber diese Variante ist besser für Flask
Base.query = db_session.query_property() #Dadurch hat jedes Base - Objekt (also auch ein Millionaire) ein Attribut query für Abfragen

class Person(Base):
    __tablename__ = 'person'  # Abbildung auf diese Tabelle

    id = Column(Integer, Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    name = Column(Text)
    age = Column(Integer)


def init_db():
    # Erzeugen der Tabellen für die Klassen, die oben deklariert sind (muss nicht sein, wenn diese schon existiert)
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
    #################################################
    # Erzeugen von Personen
    #################################################
    p1 = Person(name="Hubert", age=12) #Mit benannten Parametern
    p2 = Person(name="Herbert", age=22) #Parameter in Reihenfolge
    session = db_session.session_factory()  # Erzeugt neue Session-Objekte
    session.begin() #Starte die Transaktion
    session.add(p1)
    session.add(p2)
    session.commit() #Alle Änderungen werden an die Datenbank übertragen


    #db_session.remove()



