from fastapi import FastAPI
from config import Config

from apps.users import controllers

config = Config()
config.apply_config()
app = FastAPI()


app.include_router(controllers.router)
