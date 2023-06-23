from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from deta import Deta
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os
from pathlib import Path


app = FastAPI()

templates = Jinja2Templates(directory="static")

deta = Deta('a0xqmaete4i_YJm6uAPCWDLDJAhPYYDR2XZTHcMrisbp')
db = deta.Base('a0xqmaete4i_YJm6uAPCWDLDJAhPYYDR2XZTHcMrisbp')


class TodoItem(BaseModel):
    text: str


# Montar recursos estáticos
static_path = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")


# Ruta principal
@app.get('/')
async def index():
    file_path = os.path.join(os.getcwd(), "static", "index.html")
    with open(file_path) as file:
     return HTMLResponse(file.read())

@app.get("/top", response_class=HTMLResponse)
async def top(request: Request):
    return templates.TemplateResponse("top/top.html", {"request": request})
    
@app.get("/films")
async def get_todos():
    return []

@app.post("/films", status_code=201)
async def add_todo(item: TodoItem):
    resp = db.put(item.dict())
    return resp


# Ejecutar el servidor: uvicorn main:app --reload