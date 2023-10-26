from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates



app = FastAPI(title="HTML Aufgabe", version="0.0.1", openapi_url="/openapi.json")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    name = "Niko"
    skills = ['in process..']
    return templates.TemplateResponse("index.html", {"request": request, "name": name, "skills": skills})

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=8000)
    