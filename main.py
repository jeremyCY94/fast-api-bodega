from typing import Union

from fastapi import FastAPI
from routes.producto import producto
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://minegocioconsistema.tk",
    "https://list-producto-app-obmib.ondigitalocean.app",
    "https://ondigitalocean.app/",
    "https://list-producto-app-obmib.ondigitalocean.app/",
    "https://yatacos.store",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(producto)
