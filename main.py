from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request

from routers.algorithms import api_algorithms

app = FastAPI()

app.include_router(api_algorithms.router)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
async def testing():
    return {"hola": "Si corre"}
