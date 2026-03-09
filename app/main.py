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

@app.post("/movies")    # Adds a movie to the database via http POST
def add_movie(tmdb_id: int): # Which executes the add_movies function with the tmdb_id
    movie_credits = get_movie_credits(tmdb_id) # gets movie credits from the tmdb_id
    movie_details = get_movie_details(tmdb_id) # gets movie details from the tmdb_id
    new_movie = Movie( #adds the new movie as a movie to the database
        title = movie_details["title"], # sets title as title from TMDB details
        how_long = movie_details["runtime"], # sets how_long as runtime from TMDB details
        added_by = "default_user", # will be updated once user-system has been implemented
        tmdb_id = movie_details["id"], # sets tmdb_id as the TMBD id
        date_added = date.today(), # sets date_added as the date
        seen = False, # Update this to be an option in the future, so you can add a film you already have seen, but want the other user to see
        released = int(movie_details["release_date"][:4]), # takes the 4 first integers from tmdbs release date, which corresponds to the release year (YYYY-MM-DD)
        country = None, # Will be set at a later date
        languages = movie_details["original_language"] # sets languages as original_language from TMDB details, should be updated to be its own table at some point because of dubs, multilang etc.
    )
    db = SessionLocal()
    db.add(new_movie)
    db.commit()
    db.close()
    return "Movie added succesfully!"