from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index_api():
    return {"Name": "CoderRunner"}
