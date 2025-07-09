# schemas/housing_features.py

from pydantic import BaseModel, Field

class HousingFeatures(BaseModel):
    """
    Defines the public-facing contract for housing features.

    Uses aliases to provide user-friendly JSON field names while
    mapping to the internal attribute names that the ML model expects.
    """
    MedInc: float   = Field(..., alias="median_income", description="Median income in block group")
    HouseAge: float   = Field(..., alias="house_age", description="Median house age in block group")
    AveRooms: float   = Field(..., alias="average_rooms", description="Average number of rooms per household")
    AveBedrms: float  = Field(..., alias="average_bedrooms", description="Average number of bedrooms per household")
    Population: float = Field(..., alias="population", description="Block group population")
    AveOccup: float   = Field(..., alias="average_occupancy", description="Average number of household members")
    Latitude: float   = Field(..., alias="latitude", description="Block group latitude")
    Longitude: float  = Field(..., alias="longitude", description="Block group longitude")
