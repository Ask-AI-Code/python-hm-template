from pydantic import BaseModel


class CustomerDataSourceValidateResponse(BaseModel):
    is_valid: bool
    customer_id: str
    data_source_id: str


class BuildIndexResponse(BaseModel):
    job_id: str
    customer_id: str
    data_source_id: str
