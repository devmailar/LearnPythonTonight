from typing import Union
from fastapi import FastAPI, Request
import uuid

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    token = request.headers.get("Authorization")

    if not token:
        return {
            "description": "API register",
            "version": "0.0.1",
            "author": "Mala Vidal",
            "authorized": False,
        }

    return {
        "description": "API register",
        "version": "0.0.1",
        "author": "Mala Vidal",
        "authorized": True,
    }


@app.post("/create-table")
def create_table(request: Request):
    token = request.headers.get("Authorization")
    body = request.body()

    print(body)

    if not token:
        return {"error": "Unauthorized"}

    return {"table": "created"}
