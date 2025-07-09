# services/prediction_service.py

import numpy as np

import joblib

from config.settings import settings
from config.logging import get_logger
from schemas.housing_features import HousingFeatures

logger = get_logger(__name__)

class PredictionService:

    def __init__(self, model_path: str):
        """
        Initializes the service by loading the model from the given path.
        """
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self):
        """
        Loads the machine learning model from a file.
        """
        try:
            model = joblib.load(self.model_path)
            logger.info(f"Model loaded successfully from {self.model_path}")
            return model
        except FileNotFoundError:
            logger.error(f"Model file not found at {self.model_path}")
            return None
        except Exception as e:
            logger.error(f"An unexpected error occurred while loading the model: {e}")
            return None

    def model_is_not_loaded(self) -> bool:
        """
        Checks if model is loaded
        """
        return self.model is None

    def predict(self, features: HousingFeatures) -> float:
        """
        Generates a price prediction
        """
        if self.model_is_not_loaded():
            logger.error("Model is not loaded")
            raise RuntimeError("Model is not loaded. Cannot make predictions")

        # Convert the Pydantic model to a numpy array for the model
        feature_values = np.array(list(features.model_dump().values())).reshape(1, -1)
        prediction = self.model.predict(feature_values)
        logger.info(f"Prediction successful for features: {features.model_dump()}")

        return prediction[0]

prediction_service = PredictionService(model_path=settings.MODEL_PATH)