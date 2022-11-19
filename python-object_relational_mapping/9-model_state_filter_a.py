#!/usr/bin/python3
"""
lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    connection = engine.connect()

    Session = sessionmaker(engine)

    session = Session()

    results = session.query(State).filter(State.name.contains('a'))

    for states in results:
        print("{}: {}".format(states.id, states.name))
