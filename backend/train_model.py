import pandas as pd
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
