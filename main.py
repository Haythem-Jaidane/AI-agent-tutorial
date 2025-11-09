from fastapi import FastAPI
from models import models
from config.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "message": "Welcome to the Finance Tracker API"}
