import joblib

# One-time load at module level for efficiency
model = joblib.load('model/best_model.pkl')
scaler = joblib.load('model/scaler.pkl')

def predict_ctr(form_data):
    # Create DataFrame from form_data, scale, and predict
    import pandas as pd
    sample = pd.DataFrame([form_data])
    sample_scaled = scaler.transform(sample)
    pred = model.predict(sample_scaled)[0]
    return pred
