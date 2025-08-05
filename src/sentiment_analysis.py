import joblib

model = joblib.load('sentiment_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

def predict_sentiment(text):
    X = vectorizer.transform([text])
    return model.predict(X)[0]