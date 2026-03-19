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

import random

def download_data():
    import os
    if os.path.exists("Fake.csv") and os.path.exists("True.csv"):
        print("Using real ISOT dataset files (Fake.csv and True.csv)...")
        fake_df = pd.read_csv("Fake.csv")
        true_df = pd.read_csv("True.csv")
        fake_df['label'] = 0
        true_df['label'] = 1
        df = pd.concat([fake_df, true_df])
        # Return a sample if it's too huge to train quickly on a local PC, or full dataframe
        # df = df.sample(frac=1).reset_index(drop=True)
        return df

    print("Actual CSV files not found. Generating robust synthetic dataset for training...")
    
    # Synthetic dataset components
    fake_subjects = ["Trump", "Biden", "Elon Musk", "The President", "Celebrity", "Aliens", "Scientists"]
    fake_actions = ["died", "arrested for", "exposed in", "secretly funding", "caught with", "hiding"]
    fake_objects = ["last night", "massive scandal", "UFO hoax", "secret microchips", "illegal scheme", "illuminati"]
    fake_buzz = ["SHOCKING", "BREAKING", "EXCLUSIVE", "YOU WON'T BELIEVE", "100% REAL", "BANNED"]
    
    real_subjects = ["The government", "Senate", "Researchers", "The economy", "Global markets", "Local authorities", "Scientists"]
    real_actions = ["passed", "discovered", "reported", "announced", "projected", "investigated", "published"]
    real_objects = ["a new law", "significant growth", "a novel species", "policy changes", "budget cuts", "new infrastructure"]
    
    fake_texts = []
    real_texts = []
    
    # Generate 1500 fake news samples
    for _ in range(1500):
        headline = f"{random.choice(fake_buzz)}: {random.choice(fake_subjects)} {random.choice(fake_actions)} {random.choice(fake_objects)}!"
        if random.random() > 0.5: headline = headline.upper()
        fake_texts.append(headline.lower())
        
    # Generate 1500 real news samples
    for _ in range(1500):
        headline = f"{random.choice(real_subjects)} {random.choice(real_actions)} {random.choice(real_objects)}."
        real_texts.append(headline.lower())
        
    fake_data = pd.DataFrame({"text": fake_texts, "label": [0]*1500})
    real_data = pd.DataFrame({"text": real_texts, "label": [1]*1500})
    
    df = pd.concat([fake_data, real_data]).sample(frac=1).reset_index(drop=True)
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
