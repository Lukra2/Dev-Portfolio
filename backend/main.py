from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")

templates = Jinja2Templates(directory="../frontend/templates")

@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse(request=request, name="main.html")

if __name__ == "__main__":
    print("Rodando..")
    uvicorn.run(app="main:app", host="0.0.0.0" port=8000, reload=False)