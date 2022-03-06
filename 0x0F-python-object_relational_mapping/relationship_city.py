#!/usr/bin/python3
"""Module model_city
Defines a City table and its rows using SQLAlchemy
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base


class City(Base):
    """Class City
    Inherits from class Base to define what the table City
    looks like in a database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
