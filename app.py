from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Dockerized FastAPI!"}

@app.get("/about")
def about():
    return {"info": "This is a simple Python app running in Docker."}
