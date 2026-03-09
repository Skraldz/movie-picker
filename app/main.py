# Library imports
from fastapi import FastAPI # Imports the fastAPI functions
from database import SessionLocal # Imports the session that contains the database engine
from models import Movie, Actor, Genre # Imports the models to work in the database
from tmdb import search_movies # Imports the search movies function from tmdb.py
app = FastAPI() # The chosen API for this projects backend

@app.get("/")       # When someone makes a GET-request to /, run this function
def root():
    return {"status": "ok"}

@app.get("/movies")     # Queries the server to get all movies in the database
def get_movies():
    db = SessionLocal()     # sets database as the local session
    movies = db.query(Movie).all() # when movies is requested via a GET to this function, sets movies to be ALL movies in the (Movie) table
    db.close() # Closes the database after the query
    return movies # Returns the full added movies list to the client. 

@app.get("/search")     # Queries the server to search TMDB for an input
def search(query: str): # Defines the search function and a string query
    return search_movies(query) # Returns the response.json from the search_movies(query) in tmdb.py