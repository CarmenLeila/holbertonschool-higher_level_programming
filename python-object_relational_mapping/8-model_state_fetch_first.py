#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    """including the guard clause"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    """creating a SQLAlchemy engine that will connect to the MySQL database"""

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
