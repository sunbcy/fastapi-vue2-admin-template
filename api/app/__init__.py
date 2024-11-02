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

    # 注册插件
    register_routers(app)

    return app


# def register_routers(app):  # 只有在此处注册的应用才可以自动生成数据表
#   # 导入 APIRouter
#   from app.azquotes import azquotes_router
#   # 包含 APIRouter
#   app.include_router(azquotes_router, prefix='/api/azquotes', tags=['azquotes'])

def register_routers(app):
  from app.azquotes import routes as azquotes_routes
  app.include_router(azquotes_routes.router, prefix='/api/azquotes', tags=['azquotes'])
