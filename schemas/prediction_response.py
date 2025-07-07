# schemas/prediction_response.py

from pydantic import BaseModel

# This model defines the structure of the data will send in a response
class PredictionResponse(BaseModel):
    predicted_price: str
