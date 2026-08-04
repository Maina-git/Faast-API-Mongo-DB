from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.blog import router as blog_router


app = FastAPI(title="FastAPI Mongo Authentication")

app.include_router(auth_router)
app.include_router(blog_router)

@app.get("/")
async def root():
    return {"message": "API is running"}








