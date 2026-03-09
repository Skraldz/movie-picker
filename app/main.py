# Library imports
from fastapi import FastAPI # Imports the fastAPI functions
from database import SessionLocal # Imports the session that contains the database engine
from models import Movie, Actor, Genre # Imports the models to work in the database
from tmdb import search_movies, get_movie_details, get_movie_credits # Imports the search movies function from tmdb.py
from datetime import date # Imports the datetime library
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

@app.post("/movies")
def add_movie(tmdb_id: int):
    movie_credits = get_movie_credits(tmdb_id)
    movie_details = get_movie_details(tmdb_id)
    new_movie = Movie(
        title = movie_details["title"],
        how_long = movie_details["runtime"],
        added_by = "default_user", # will be updated once user-system has been implemented
        tmdb_id = movie_details["id"],
        date_added = date.today(),
        seen = False, # Update this to be an option in the future, so you can add a film you already have seen, but want the other user to see
        released = int(movie_details["release_date"][:4]),
        country = None, # kunne ikke finde korrekte detalje
        languages = movie_details["original_language"]
    )
    db = SessionLocal()
    db.add(new_movie)
    db.commit()
    db.close()
    return "Movie added succesfully!"