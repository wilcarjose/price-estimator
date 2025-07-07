# main.py

from fastapi import FastAPI

app = FastAPI(
    title="Housing Price Predictor",
    description="An API to predict median house values using a trained ML model.",
    version="1.0.0"
)

@app.get("/")
def welcome_message():
    """
    Welcome endpoint for the API
    """
    return {"message": f"Welcome to the {app.title} version {app.version}. Go to /docs for the API documentation"}
