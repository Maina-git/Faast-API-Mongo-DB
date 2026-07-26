from fastapi import FastAPI
from app.routes.auth import router as auth_router

app = FastAPI(title="FastAPI Mongo Authentication")

app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "API is running"}








