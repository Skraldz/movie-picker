from dotenv import load_dotenv # Imports the extension that can read .env files
import os # A library that gives access to the OS environment variables (the .env file)
import httpx # A library that enables HTTP requests to external API's (In this case TMDB)

load_dotenv(dotenv_path="../.env") # Starts up dotenv, so the token can be read from the .env file

token = os.getenv("TMDB_API_TOKEN") # Sets token variable to be the TMDB API token collected from the .env file'

def search_movies(query):   # Function that searches TMDB for a match with users search input
    headers = {"Authorization": f"Bearer {token}"}  # adds the TMDB API token in the header of the GET to TMDB's API
    response = httpx.get("https://api.themoviedb.org/3/search/movie", # Sets the response variable as the results from the GET request to TMDBs API
      headers=headers, # Includes the API token header in the GET request
      params={"query": query} # Sets the search parameters to be the user input on the client side
   ) 
    return response.json() # Returns the TMDB search query to the user

def get_movie_details(tmdb_id): # Function that gets details on a movie based on TMDB data
   headers = {"Authorization": f"Bearer {token}"} # adds the TMDB API token in the header of the GET to TMDB's API
   response = httpx.get(f"https://api.themoviedb.org/3/movie/{tmdb_id}", # Sets the response variable as the results from the GET request to TMDBs API
      headers=headers, # Includes the API token header in the GET request
   )
   return response.json() # Returns the TMDB movie details in .json

def get_movie_credits(tmdb_id): # Function that gets movie credits based on TMDB data
   headers = {"Authorization": f"Bearer {token}"} # Adds the TMDB API token in the header
   response = httpx.get(f"https://api.themoviedb.org/3/movie/{tmdb_id}/credits", # Sets the response variable as the results from the GET request to TMDBs API
      headers=headers, # Includes the API token header in the GET request
   )
   return response.json() # Returns the TMDB credits in .json