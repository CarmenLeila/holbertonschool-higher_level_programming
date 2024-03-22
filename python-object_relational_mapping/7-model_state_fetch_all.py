#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    """including the guard clause"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username,
        password,
        database
    ), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()

    session.close()

    for state in query:
        print("{}: {}".format(state.id, state.name))
