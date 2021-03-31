import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)   
    name=Column(String(250), nullable=False)
    height=Column(Float)
    mass=Column(Integer)
    gender=Column(String(250))
    homeworld=Column(String(250))
    image=Column(String(250))
    born=Column(Integer)
    died=Column(Integer)
    species=Column(String(250))
    cybernetics=Column(String(250))

class planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)   
    name=Column(String(250), nullable=False)
    diameter=Column(Integer)
    rotation_period=Column(Integer)
    orbital_period=Column(Integer)
    surface_water=Column(Integer)
    gravity=Column(String(250))
    terrain=Column(String(250))
    population=Column(Integer)

class users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)   
    name=Column(String(250), nullable=False)
    password=Column(String(250), nullable=False)

class favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    users_id=Column(Integer, ForeignKey('users.id'))
    planets_id=Column(Integer, ForeignKey('planets.id'))
    characters_id=Column(Integer, ForeignKey('characters.id'))  

def to_dict(self):
     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')