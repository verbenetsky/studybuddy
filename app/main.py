from fastapi import FastAPI

app = FastAPI(title="StudyBuddy")


@app.get("/")
def read_root():
    return {"message": "Hello World"}
