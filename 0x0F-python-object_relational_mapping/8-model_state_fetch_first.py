#!/usr/bin/python3
"""Module 8-model_state_fetch_first
Fetches the first row in the states table
of the database passed as argument
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Program starts here.
    Using SQLAlchemy, the 'states' table is loaded and
    the first entry in the table is printed. If there's no row,
    'Nothing' is printed"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_found = session.query(State)

    if len(states_found.all()):
        print(str(states_found.all()[0].id) +
              ": " + states_found.all()[0].name)
    else:
        print("Nothing")


if __name__ == "__main__":
    main()
