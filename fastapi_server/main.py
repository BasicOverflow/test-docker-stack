import threading
from fastapi import FastAPI
import requests

app = FastAPI()

# def yeah():
#     callback_url = "http://microservice1:81/test"
#     response = requests.get(callback_url)
#     print(response.text)  

# threading.Thread(target=yeah).start()

@app.get("/")
def read_root():
    return {"Hello": "poo"}


@app.get("/callback") 
async def callback():
    '''route that calls function to make call to other microservice'''
    # make a callback to another server
    callback_url = "http://microservice1:81/test" 
    response = requests.get(callback_url)
    
    # handle the response from the other server
    # ...
    
    return {"data from microservice": response.text}

