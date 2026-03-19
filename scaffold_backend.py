import os

backend_files = {
    "backend/app/__init__.py": "",
    "backend/app/schemas.py": """from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    text: str = Field(..., min_length=20, description="The news text to classify")
    model_name: str = Field("Logistic Regression", description="The ML model to use")

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    explanation: list
""",
    "backend/app/utils.py": """import re
import string

def preprocess_text(text: str) -> str:
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove extra spaces
    text = re.sub(r'\\s+', ' ', text).strip()
    return text
""",
    "backend/app/models.py": """class MLModelManager:
    def __init__(self):
        self.models = {}
        self.vectorizer = None
    
    def load_models(self):
        import joblib
        import os
        model_dir = os.path.join(os.path.dirname(__file__), '../models')
        try:
            self.vectorizer = joblib.load(os.path.join(model_dir, 'vectorizer.joblib'))
            self.models['Logistic Regression'] = joblib.load(os.path.join(model_dir, 'lr_model.joblib'))
            self.models['Multinomial Naive Bayes'] = joblib.load(os.path.join(model_dir, 'nb_model.joblib'))
            self.models['Random Forest'] = joblib.load(os.path.join(model_dir, 'rf_model.joblib'))
            return True
        except Exception as e:
            print(f"Models not found, please train first: {e}")
            return False

model_manager = MLModelManager()
""",
    "backend/app/main.py": """from fastapi import FastAPI, HTTPException, Request
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
""",
    "backend/train_model.py": """import pandas as pd
import numpy as np
import os
import urllib.request
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def download_data():
    print("Downloading ISOT dataset...")
    # Placeholder URLs - ISOT is large so we simulate a smaller download or require manual download
    # In a real scenario, use kagglehub or direct urls.
    # We will create a dummy dataset for demonstration if not found.
    if not os.path.exists("Fake.csv"):
        print("Creating mock dataset for training...")
        fake_data = pd.DataFrame({"text": ["Fake news is everywhere", "Aliens landed exactly here!"], "label": [0, 0]})
        real_data = pd.DataFrame({"text": ["The government passed a new law.", "Scientists discover new species."], "label": [1, 1]})
        df = pd.concat([fake_data, real_data])
    else:
        fake_df = pd.read_csv("Fake.csv")
        true_df = pd.read_csv("True.csv")
        fake_df['label'] = 0
        true_df['label'] = 1
        df = pd.concat([fake_df, true_df])
    return df

def main():
    df = download_data()
    X = df['text']
    y = df['label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Vectorizing text...")
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Multinomial Naive Bayes': MultinomialNB(),
        'Random Forest': RandomForestClassifier(n_estimators=10, random_state=42) # reduced estimators for speed
    }
    
    os.makedirs('models', exist_ok=True)
    joblib.dump(vectorizer, 'models/vectorizer.joblib')
    
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train_vec, y_train)
        preds = model.predict(X_test_vec)
        acc = accuracy_score(y_test, preds)
        print(f"{name} Accuracy: {acc:.4f}")
        
        filename = ''
        if name == 'Logistic Regression': filename = 'lr_model.joblib'
        elif name == 'Multinomial Naive Bayes': filename = 'nb_model.joblib'
        else: filename = 'rf_model.joblib'
        
        joblib.dump(model, f'models/{filename}')
        
    print("Training complete. Models saved.")

if __name__ == "__main__":
    main()
""",
    "backend/requirements.txt": """fastapi==0.103.1
uvicorn==0.23.2
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.25.2
joblib==1.3.2
""",
    "backend/Dockerfile": """FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
""",
    "backend/.env.example": "PORT=8000\n"
}

for path, content in backend_files.items():
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
print("Backend scaffolded successfully.")
