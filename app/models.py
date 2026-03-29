# Library imports - imports functions from sqlalchemy
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): # The main interaction between our database and python - Declarative base is the way we add entries to each table
    pass  # Passes on arguments

class Movie(Base): # Creates a class for the table movies in the database
    __tablename__ = "movies" # Assigns the class to the table name in the database
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    how_long = Column(Integer)
    added_by = Column(String(255))
    tmdb_id = Column(String(255))
    date_added = Column(Date)
    seen = Column(Boolean)
    released = Column(Integer)
    country = Column(String(255))
    languages = Column(String(255))

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    actor_name = Column(String(255))

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    genre = Column(String(255))

class Movie_genres(Base):   # Creates a class for the table movie_genres in the database
    __tablename__ = "movie_genres" # Assigns the class to the table name
    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True) # sets a column to contain the variable movie_id as an integer with the id value of the movies in the movies table, and sets it as a primary key in this table
    genre_id = Column(Integer, ForeignKey("genres.id"), primary_key=True) # sets a column to contain the variable genre_id as an integer with the id value of the genre in the genres table, and sets it as a primary key in this table

class Movie_actors(Base):
    __tablename__ = "movie_actors"
    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True)
    actor_id = Column(Integer, ForeignKey("actors.id"), primary_key=True)