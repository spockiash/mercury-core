# services/ingestion/app/main.py

from fastapi import FastAPI
from api.routes import router as api_router

app = FastAPI(title="Mercury Ingestion Service")

app.include_router(api_router)
