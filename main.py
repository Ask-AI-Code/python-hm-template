from fastapi import FastAPI
from fastapi.responses import JSONResponse

from tasks import create_task

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def say_hello(name: str):
    return {"isWorking": True}


@app.post("/task")
async def post_task(message: str):
    task = create_task.delay(message)
    return JSONResponse({"task_id": task.id})
