import itertools
import datetime
from typing import List, Optional
import uuid
import random
import string
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


import dynamodb_local as db


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str


class Tasks(BaseModel):
    name: Optional[str] = None
    title: str


app = FastAPI()

today_data = datetime.datetime.now().strftime("%Y%m%d")

origins = [
    "http:///127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/tasks")
async def get_single_task(request: Request, task_id: str):
    res = None
    if not task_id:
        res = db.get_all_tasks()
    else:
        res = db.get_task(task_id)

    return res


@app.post("/tasks")
async def create_task(request: Request, data: Tasks):

    task_id = get_random_string(4)
    print(task_id)
    task_data = {"task_id": task_id, "name": data.name, "title": data.title}

    db.create_task(task_data)

    return {"method": request.method}


@app.api_route("/tasks", methods=["DELETE"])
async def test(request: Request, data: dict):
    print(request.method, flush=True)

    print(data)
    return {"method": request.method}
