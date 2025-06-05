from fastapi import FastAPI
from .routers import health

app = FastAPI(title="Blue Magnitude API", version="0.0.1")
app.include_router(health.router)
