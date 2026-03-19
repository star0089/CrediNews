from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    text: str = Field(..., min_length=20, description="The news text to classify")
    model_name: str = Field("Logistic Regression", description="The ML model to use")

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    explanation: list
