class MLModelManager:
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
