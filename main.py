from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from core.executor import exec_run_python, get_container

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



def runcode_action(form: CodeRunForm):
    LANGUAGES = {
        "python": get_container('codebox-python3'),
        "python3": get_container('codebox-python3')
    }
    if form.language  not in LANGUAGES:
        return {"result": "Unsupported language", "code": 400}

    user = "codemax"

    container = LANGUAGES[form.language]

    result = exec_run_python(container, form.code, user)

    return {"result": result, "code": 0}


@app.post("/api/coderun/")
def codecode_api(form: CodeRunForm):
    return runcode_action(form)


@app.post("/api/runcode/")
def runcode_api(form: CodeRunForm):
    return runcode_action(form)
