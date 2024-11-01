import os
import datetime
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.utils import responses as resp
from app.utils.responses import response_with


def create_app():
    app = FastAPI()

    app.mount("/static", StaticFiles(directory="../dist/static", html=True), name="static")

    templates = Jinja2Templates(directory="../dist")

    return app


