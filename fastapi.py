from fastapi import FastAPI
from pydantic import BaseModel
from pipeline.scam_detector.detector import ScamDetector

app = FastAPI()

detector = ScamDetector()

class Message(BaseModel):
    text: str

@app.post("/detect")
def detect(message: Message):
    result = detector.detect(message.text)
    return {"result": result}

@app.get("/")
def home():
    return {"message": "Scam Detector API is running"}