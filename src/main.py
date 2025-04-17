from fastapi import FastAPI
from src.resonators.router import router as resonators_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}


app.include_router(resonators_router)
