from typing import Union
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Pee"}


@app.get("/callback")
async def callback():
    # make a callback to another server
    callback_url = "http://example.com/callback"
    response = requests.get(callback_url)
    
    # handle the response from the other server
    # ...
    
    return {"message": "Callback completed successfully"}


# create route that calls function to make call to other microservice