import joblib
import numpy as np
import os

MODEL_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'models', 'stress_predictor.pkl'
)

def load_model():
    return joblib.load(MODEL_PATH)

def predict_stress(rent, income, transport, groceries,
                   tuition, study_hours, work_hours, commute):
    model = load_model()
    features = np.array([[rent, income, transport, groceries,
                          tuition, study_hours, work_hours, commute]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    return {
        'stressed': bool(prediction),
        'probability': round(float(probability) * 100, 1),
        'label': 'At risk' if prediction else 'Stable',
    }