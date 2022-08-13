from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from core.executor import exec_run_python
from core.docker_client import DockerClient


app = FastAPI()
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class CodeRunForm(BaseModel):
    language: str
    version: Optional[str] = "0.01"
    code: str
    timestamp: int


@app.get("/")
def index_api():
    version = "0.0.1"
    return {"Name": "CoderRunner", "Version": version}


@app.post("/api/coderun/")
def runcode_api(form: CodeRunForm):
    container = DockerClient.containers.get('py3mod')

    user = "codemax"
    result = exec_run_python(container, form.code, user)

    return {"result": result, "code": 0}
