# config/settings.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Defines the application's configuration settings
    """
    APP_NAME: str = "Housing Price Predictor"
    APP_DESCRIPTION: str = "An API to predict median house values using a trained ML model."
    APP_VERSION: str = "1.0.0"
    MODEL_PATH: str = "models/housing_price_model.joblib"

    # Looks for settings in a .env file.
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Create a single instance of the Settings class that can be imported
settings = Settings()
