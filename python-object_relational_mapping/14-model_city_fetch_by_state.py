#!/usr/bin/python3
""" a script that prints all City objects from the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    """SQLAlchemy engine that will connect to the MySQL database"""

    # Creation of a  session to interact with the DB
    Session = sessionmaker(bind=engine)
    session = Session()

    for cities, states in (session.query(City, State)
                           .join(State, City.state_id == State.id)
                           .order_by(City.id)):
        print(f"{states.name}: ({cities.id}) {cities.name}")
