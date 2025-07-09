# api/v1/endpoints.py

from fastapi import APIRouter, Depends, HTTPException

from schemas.housing_features import HousingFeatures
from schemas.prediction_response import PredictionResponse
from services.prediction_service import prediction_service

router = APIRouter()

def get_prediction_service():
    if prediction_service.model_is_not_loaded():
        raise HTTPException(
            status_code=400,
            detail="Model is not loaded"
        )
    return prediction_service

@router.post("/predict", response_model=PredictionResponse)
async def predict(
    features: HousingFeatures,
    service = Depends(get_prediction_service)
):
    """
    Return the predict media value
    """
    raw_prediction = service.predict(features)
    predicted_price = raw_prediction * 100000
    formated_price = f"${predicted_price:,.2f}"
    return {"predicted_price": formated_price}
