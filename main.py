from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from database import Base, engine, get_db
from models import User

app = FastAPI()

# Create all tables in the database
Base.metadata.create_all(bind=engine)

@app.get("/")
def create_user():
    return {"message": "Hello World"}
