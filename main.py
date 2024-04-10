# main.py

from fastapi import FastAPI
from blog.routers import user as user_router

app = FastAPI()

app.include_router(user_router.router)
