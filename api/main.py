import warnings

from app import create_app
from fastapi.responses import FileResponse

warnings.simplefilter("ignore")
app = create_app()


@app.get("/")
async def index():
    return FileResponse("../dist/index.html")

