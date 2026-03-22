from fastapi import FastAPI, HTTPException 
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel 
from transformers import pipeline 
import os, logging, time 
 
logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__) 
 
APP_ENV = os.getenv("APP_ENV", "dev") 
MODEL_NAME = os.getenv("MODEL_NAME", "distilbert-base-uncased-finetuned-sst-2-english") 
 
app = FastAPI(title="MLOps Sentiment Analysis API", version="1.0.0") 
 
sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_NAME) 
 
class TextInput(BaseModel): 
    text: str 
 
@app.get("/") 
def root(): 
    return {"message": "MLOps Sentiment API", "environment": APP_ENV} 
 
@app.get("/health") 
def health(): 
    return {"status": "healthy", "environment": APP_ENV} 
 
@app.get("/ready") 
def ready(): 
    return {"status": "ready", "model_loaded": True} 
 
@app.post("/predict") 
def predict(input: TextInput): 
    start = time.time() 
    result = sentiment_pipeline(input.text)[0] 
    latency = (time.time() - start) * 1000 
    return {"text": input.text, "label": result["label"], "score": round(result["score"], 4), "environment": APP_ENV, "latency_ms": round(latency, 2)} 
