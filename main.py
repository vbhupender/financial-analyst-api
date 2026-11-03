
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello World" , "status": "Financial Analyst API Active"}

