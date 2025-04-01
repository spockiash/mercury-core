# services/ingestion/app/main.py
import debugpy
from fastapi import FastAPI
from api.routes import router as api_router

debugpy.listen(("0.0.0.0", 5678))
debugpy.wait_for_client()

message = "I have intercepted this value from DAP"
print(message)

app = FastAPI(title="Mercury Ingestion Service")

app.include_router(api_router)
