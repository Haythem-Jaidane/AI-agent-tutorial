from fastapi import FastAPI
from models import models
from config.database import engine
from routes.transactions import router as transactions_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(transactions_router)

@app.get("/")
def read_root():
    return {"Hello": "World", "message": "Welcome to the Finance Tracker API"}
