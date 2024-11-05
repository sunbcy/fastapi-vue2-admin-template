import os
import datetime
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils import responses as resp
from utils.responses import response_with


def create_app():
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="../dist/static", html=True), name="static")
    templates = Jinja2Templates(directory="../dist")
    # 注册插件
    register_routers(app)
    return app


def register_routers(app):  # 只有在此处注册的应用才可以自动生成数据表
    from app.azquotes import routes as azquotes_routes
    app.include_router(azquotes_routes.router, prefix='/api/azquotes', tags=['azquotes'])

    from app.system_info import routes as system_info_routes
    app.include_router(system_info_routes.router, prefix='/api/system_info', tags=['system_info'])
