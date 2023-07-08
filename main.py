from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from data_classes import BuildIndexResponse, CustomerDataSourceValidateResponse

from tasks import create_task

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get(
    "/customers/{customer_id}/data_sources/{data_source_id}/validate",
    response_model=CustomerDataSourceValidateResponse,
)
async def get_customer_data_source_validate(customer_id: str, data_source_id: str):
    return CustomerDataSourceValidateResponse(
        is_valid=False,
        customer_id=customer_id,
        data_source_id=data_source_id,
    )


@app.post(
    "/customers/{customer_id}/data_sources/{data_source_id}/build_index",
    response_model=BuildIndexResponse,
)
async def post_build_index_job(customer_id: str, data_source_id: str):
    return BuildIndexResponse(
        job_id="unknown",
        customer_id=customer_id,
        data_source_id=data_source_id,
    )


@app.post("/customers/{customer_id}/data_sources/{data_source_id}/key")
async def post_data_source_key(customer_id: str, data_source_id: str):
    return Response(status_code=204)


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
