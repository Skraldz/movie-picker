# Library imports
from fastapi import FastAPI # Imports the fastAPI functions
from database import SessionLocal # Imports the session that contains the database engine
from models import Movie, Actor, Genre, Movie_genres, Movie_actors # Imports the models to work in the database
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
    movie_credits = get_movie_credits(tmdb_id) # TODO: implement actor saving to movie_actors table
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
    db = SessionLocal() # Sets database as the local session
    db.add(new_movie) # adds (new_movie) to the database
    db.commit() # commits the changes to the database
    db.refresh(new_movie) # Refreshes the movie variable so it contains the unique database ID it gets when commited

    for genre in movie_details["genres"]: # For-loop for genre in movie_details (TMDB's genre)
        existing_genre = db.query(Genre).filter(Genre.genre == genre["name"]).first() # existing_genre = query the database model [Genre] with a filter that searches the [Genre] table to see if there already exists a genre in the database with the same name as the TMDB genre name
        if not existing_genre: # If there isn't a matching genre in the [Genre] table
            new_genre = Genre(genre=genre["name"]) # Set new_genre = TMDB genre name, as a genre object in the [Genre] table
            db.add(new_genre) # Add the genre to the database
            db.commit() # Commit the changes
            db.refresh(new_genre) # Refreshes the genre variable so it contains the unique database ID it gets when commited
        
        genre_to_link = existing_genre if existing_genre else new_genre # makes the genre_to_link variable into the genre variable, if it's an existing or new one
        movie_genre_link = Movie_genres(
        movie_id = new_movie.id,
        genre_id = genre_to_link.id
        )
        db.add(movie_genre_link)
        db.commit()

    for cast in movie_credits["cast"][:10]:
        existing_actor = db.query(Actor).filter(Actor.actor_name == cast["name"]).first()
        if not existing_actor:
            new_actor = Actor(actor_name=cast["name"])
            db.add(new_actor)
            db.commit()
            db.refresh(new_actor)

        actor_to_link = existing_actor if existing_actor else new_actor
        movie_actor_link = Movie_actors(
            movie_id = new_movie.id,
            actor_id = actor_to_link.id
        )
        db.add(movie_actor_link)
        db.commit()
    db.close() # closes the database
    return "Movie added succesfully!"  

@app.get("/movies/pick")
def pick_movie(genre: str = None, max_length: int = None, seen: bool = None, released_from: int = None, released_to: int = None, actor: str = None):
    db = SessionLocal()     # sets database as the local session
    query = db.query(Movie) # when movies is requested via a GET to this function ..
    
    if seen is not None: # If the seen filter is NOT None
        query = query.filter(Movie.seen == seen) # filters the query after the selected filter (seen or not seen)
    if max_length is not None:
        query = query.filter(Movie.how_long <= max_length)
    if released_from is not None:
        query = query.filter(Movie.released >= released_from)
    if released_to is not None:
        query = query.filter(Movie.released <= released_to)
    if genre is not None:
        query = query.join(Movie_genres).join(Genre).filter(Genre.genre == genre)
    if actor is not None:
        query = query.join(Movie_actors).join(Actor).filter(Actor.actor_name == actor)
    
    
    db.close() # Closes the database after the query
    return query # Returns the full added movies list to the client. 

    


 