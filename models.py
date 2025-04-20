from beanie import Document, Link
from pydantic import BaseModel


class PredictionModel(Document):
    image_id: str
    label: str
    confidence: float

    class Settings:
        name = 'predictions'


class PredictionRequest(BaseModel):
    file: bytes
