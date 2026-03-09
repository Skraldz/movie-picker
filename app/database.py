from sqlalchemy import create_engine # imports the create_engine function from sqlalchemy
from dotenv import load_dotenv # Imports the extension that can read .env files
import os # A library that gives access to the OS environment variables (the .env file)
from sqlalchemy.orm import sessionmaker # imports the sessionmaker function

load_dotenv() # Starts up dotenv, so the password can be picked from the .env file

password = os.getenv("MOVIE_PICKER_DB_PASSWORD") # Sets password to be the mysqlroot password collected from the .env file

DATABASE_URL = f"mysql+pymysql://movie_picker_user:{password}@192.168.5.10:3306/movie_db" # Where on which machine my database is located

engine = create_engine(DATABASE_URL) # Creates the engine for my database, so it can interact with main.py

SessionLocal = sessionmaker(bind=engine) # Makes a session and binds it to the engine, so it can interact with the tables