import pandas as pd
import numpy as np
import os
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import random

def clean_text(text):
    if not isinstance(text, str): return ""
    # Strip URLS
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Strip Reuters and city prefixes: e.g. "WASHINGTON (Reuters) -" or "New York - "
    text = re.sub(r'^.*?-\s*', '', text)
    # Strip standard twitter handles
    text = re.sub(r'\@\w+|\#', '', text)
    return text.lower()

def download_data():
    df_list = []
    import os
    if os.path.exists("Fake.csv") and os.path.exists("True.csv"):
        print("Loading real ISOT dataset files...")
        fake_df = pd.read_csv("Fake.csv")
        true_df = pd.read_csv("True.csv")
        
        print("Aggressively scrubbing ISOT biases (URLs, Publisher tags, City prefixes)...")
        true_df['text'] = true_df['text'].apply(clean_text)
        fake_df['text'] = fake_df['text'].apply(clean_text)
        
        fake_df['label'] = 0
        true_df['label'] = 1
        isot_df = pd.concat([fake_df, true_df])
        df_list.append(isot_df)

    print("Generating advanced synthetic news to reinforce modern queries...")
    fake_subjects = ["Trump", "Biden", "Elon Musk", "The President", "Celebrity", "Aliens", "Scientists", "Government"]
    fake_actions = ["died", "arrested for", "exposed in", "secretly funding", "caught with", "hiding", "faked", "banned"]
    fake_objects = ["last night", "massive scandal", "UFO hoax", "secret microchips", "illegal scheme", "illuminati"]
    fake_buzz = ["SHOCKING", "BREAKING", "EXCLUSIVE", "YOU WON'T BELIEVE", "100% REAL", "BANNED"]
    
    real_subjects = ["The government", "Senate", "Researchers", "The economy", "Global markets", "Local authorities", "Police"]
    real_actions = ["passed", "discovered", "reported", "announced", "projected", "investigated", "published", "stated"]
    real_objects = ["a new law", "significant growth", "a novel species", "policy changes", "budget cuts", "infrastructure"]
    
    fake_texts, real_texts = [], []
    for _ in range(5000):
        fake_texts.append(f"{random.choice(fake_buzz)}: {random.choice(fake_subjects)} {random.choice(fake_actions)} {random.choice(fake_objects)}!".lower())
        real_texts.append(f"{random.choice(real_subjects)} {random.choice(real_actions)} {random.choice(real_objects)}.".lower())
        
    synth_df = pd.concat([
        pd.DataFrame({"text": fake_texts, "label": [0]*5000}),
        pd.DataFrame({"text": real_texts, "label": [1]*5000})
    ])
    df_list.append(synth_df)
    
    final_df = pd.concat(df_list).sample(frac=1).reset_index(drop=True)
    return final_df


def main():
    df = download_data()
    # Drop empty rows
    df = df.dropna(subset=['text'])
    df = df[df['text'].str.len() > 10]
    
    X = df['text']
    y = df['label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
    
    print("Vectorizing with Advanced N-Grams (Bigrams included)...")
    # Bi-grams help capture 'donald trump' or 'passed law'
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10000, ngram_range=(1, 2), min_df=3)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, C=1.5),
        'Multinomial Naive Bayes': MultinomialNB(alpha=0.5),
        'Random Forest': RandomForestClassifier(n_estimators=30, random_state=42, n_jobs=-1)
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
