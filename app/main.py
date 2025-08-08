from fastapi import FastAPI
from app.api.v1.endpoints import auth

app = FastAPI(title="APA Pool League API", version="1.0.0")

@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "ok", "message": "API is running!"}

app.include_router(auth.router, prefix="/api/v1", tags=["Authentication"])