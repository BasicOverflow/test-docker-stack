import httpx
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "poo"}


@app.get("/callback") 
async def callback():
    '''route that calls function to make call to other microservice'''
    # make a callback to another server
    async with httpx.AsyncClient() as client:
        callback_url = "http://microservice1:81/test" 
        data = await client.get(callback_url)
    
    # handle the response from the other server
    # ...
    
    return {"data from microservice": data}

