# main.py

from fastapi import FastAPI

from api.v1.endpoints import router as v1_router

app = FastAPI(
    title="Housing Price Predictor",
    description="An API to predict median house values using a trained ML model.",
    version="1.0.0"
)

app.include_router(v1_router, prefix="/api/v1", tags=["Version 1"])

@app.get("/")
def welcome_message():
    """
    Welcome endpoint for the API
    """
    return {"message": f"Welcome to the {app.title} version {app.version}. Go to /docs for the API documentation"}
