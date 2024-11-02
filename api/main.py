import warnings

from app import create_app
from fastapi.responses import FileResponse

warnings.simplefilter("ignore")
app = create_app()


@app.get("/")
async def index():
    return FileResponse("../dist/index.html")

# 启动应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
