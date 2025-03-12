from fastapi import FastAPI
from .routers import aws

app = FastAPI()

app.include_router(aws.router)
