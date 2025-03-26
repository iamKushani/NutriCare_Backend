from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import subprocess


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)
# Create the second FastAPI instance
app2 = FastAPI()

# Configure CORS for the second instance
app2.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


class Message(BaseModel):
    user: str
    text: str


messages = []

class Message(BaseModel):
    user: dict


