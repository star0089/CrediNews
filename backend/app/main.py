from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import time
from .schemas import PredictionRequest, PredictionResponse
from .utils import preprocess_text
from .models import model_manager

app = FastAPI(title="CrediNews API", description="AI-Assisted Fake News Detection System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic Rate limiting (In-memory, for demo purposes)
request_history = {}

@app.on_event("startup")
def startup_event():
    model_manager.load_models()

@app.post("/predict", response_model=PredictionResponse)
async def predict(req: PredictionRequest, request: Request):
    # Rate Limiting: 10 reqs per minute per IP
    client_ip = request.client.host
    now = time.time()
    if client_ip not in request_history:
        request_history[client_ip] = []
    
    # Clean old requests
    request_history[client_ip] = [t for t in request_history[client_ip] if now - t < 60]
    if len(request_history[client_ip]) >= 10:
        raise HTTPException(status_code=429, detail="Too many requests. Limit is 10 per minute.")
    request_history[client_ip].append(now)

    if not model_manager.vectorizer:
        raise HTTPException(status_code=503, detail="Models are not loaded. Please train first.")
        
    if req.model_name not in model_manager.models:
        raise HTTPException(status_code=400, detail="Invalid model name selected.")
        
    # Preprocess
    cleaned_text = preprocess_text(req.text)
    
    # Vectorize
    vec_text = model_manager.vectorizer.transform([cleaned_text])
    
    # Predict
    model = model_manager.models[req.model_name]
    pred = model.predict(vec_text)[0]
    prob = model.predict_proba(vec_text)[0]
    
    confidence = float(max(prob) * 100)
    label = "REAL" if pred == 1 else "FAKE"
    
    # Simple Explanation (Top 5 words)
    words = model_manager.vectorizer.inverse_transform(vec_text)[0]
    explanation = list(words[:5]) if len(words) > 0 else ["No significant words found"]

    return PredictionResponse(
        prediction=label,
        confidence=confidence,
        explanation=explanation
    )



