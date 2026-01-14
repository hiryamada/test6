from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AdditionRequest(BaseModel):
    a: float
    b: float


class AdditionResponse(BaseModel):
    result: float


@app.get("/")
async def root():
    return {"message": "Addition API"}


@app.post("/add", response_model=AdditionResponse)
async def add(request: AdditionRequest):
    result = request.a + request.b
    return AdditionResponse(result=result)
