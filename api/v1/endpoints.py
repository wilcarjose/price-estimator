# api/v1/endpoints.py

from fastapi import APIRouter

from schemas.prediction_response import PredictionResponse

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict():
    """
    Return the predict media value
    """
    predict_price = 123456
    formated_price = f"${predict_price:,.2f}"

    return {"predicted_price": formated_price}
