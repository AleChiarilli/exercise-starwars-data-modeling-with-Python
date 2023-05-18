import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorites_planets = relationship('FavoritesPlanets', backref='user', lazy=True)
    favorites_characters = relationship('FavoritesCharacters', backref='user', lazy=True)
    favorites_vehicles = relationship('Favoritesvehicles', backref='user', lazy=True)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    size = Column(String(250))
    population = Column(String(250), nullable=False)
    favorites_planets = relationship('FavoritesPlanets', backref='planets', lazy=True)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    gender = Column(String(250))
    birth_year = Column(String(250), nullable=False)
    planet_ID = Column(String(250), nullable=False)
    favorites_character = relationship('FavoritesCharacters', backref='characters', lazy=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250))
    speed = Column(String(250))
    model = Column(String(250), nullable=False)
    favorites_vehicles = relationship('FavoritesVehicles', backref='vehicles', lazy=True)


class FavoritesPlanets(Base):
    __tablename__ = "favoritesplanets"
    id = Column (Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class FavoritesCharacters(Base):
    __tablename__ = "favoritescharacters"
    id = Column (Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)

class FavoritesVehicles(Base):
    __tablename__ = "favoritesvehicles"
    id = Column (Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
