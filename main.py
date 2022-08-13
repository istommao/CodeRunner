from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

from core.executor import exec_run_python
from core.docker_client import DockerClient


app = FastAPI()


class CodeRunForm(BaseModel):
    language: str
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
