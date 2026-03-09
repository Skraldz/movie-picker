from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = "movies"
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