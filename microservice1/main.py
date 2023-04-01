from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def read_root():
    return "Data from microservice1 blah blah"
