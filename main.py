# main.py

from fastapi import FastAPI

from api.v1.endpoints import router as v1_router
from config.settings import settings
from config.logging import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)

@app.on_event("startup")
def on_startup():
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}...")

app.include_router(v1_router, prefix="/api/v1", tags=["Version 1"])

@app.get("/")
def welcome_message():
    """
    Welcome endpoint for the API
    """
    return {"message": f"Welcome to the {settings.APP_NAME} version {settings.APP_VERSION}. Go to /docs for the API documentation"}
