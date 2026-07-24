from fastapi import FastAPI
from pydantic import BaseModel

from .ocr import extract_text
from .gemini import extract_fields
from .matcher import find_match
from .risk_engine import assess_risk


app = FastAPI(
    title="TrueMeds API",
    version="1.0"
)


class ImageRequest(BaseModel):
    image_path: str


@app.get("/")
def home():

    return {
        "message": "TrueMeds Backend Running"
    }


@app.post("/verify")
def verify_medicine(request: ImageRequest):

    # OCR
    ocr_result = extract_text(request.image_path)

    # Gemini
    fields = extract_fields(
        ocr_result["ocr_text"]
    )
    print(type(fields))
    print(fields)
    # Matcher
    match = find_match(fields)

    # Risk Engine
    report = assess_risk(
        match,
        fields
    )

    return report