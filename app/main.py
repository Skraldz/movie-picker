# Library imports
from fastapi import FastAPI
app = FastAPI()

@app.get("/")       # When someone makes a GET-request to /, run this function
def root():
    return {"status": "ok"}