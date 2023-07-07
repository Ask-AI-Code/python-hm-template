from fastapi import FastAPI
from fastapi.responses import JSONResponse

from tasks import create_task

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/customers/{customer_id}/data_sources/{data_source_id}/validate")
async def get_customer_data_source_validate(customer_id: str, data_source_id: str):
    return {
        "validated": False,
        "customer_id": customer_id,
        "data_source_id": data_source_id,
    }


@app.post("/customers/{customer_id}/data_sources/{data_source_id}/build_index")
async def post_build_index_job(customer_id: str, data_source_id: str):
    return {
        "job_id": "unknown",
        "customer_id": customer_id,
        "data_source_id": data_source_id,
    }


@app.post("/task")
async def post_task(message: str):
    task = create_task.delay(message)
    return JSONResponse({"task_id": task.id})


@app.get("/task/{task_id}")
async def post_task(task_id: str):
    task = create_task.AsyncResult(task_id)
    return JSONResponse(
        {"task_id": task_id, "status": task.status, "result": task.result}
    )
