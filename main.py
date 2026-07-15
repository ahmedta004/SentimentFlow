# Import FastAPI from fastapi
from fastapi import FastAPI
# Import BaseModel from pydantic
from pydantic import BaseModel
# Import joblib 
import joblib
# Import TextPreprocessor from text_preprocessor
from text_preprocessor import TextPreprocessor

# Initialize the FastAPI application and store it in a variable named app
app = FastAPI()

# Define a Pydantic model named FeedbackRequest that inherits from BaseModel
class FeedbackRequest(BaseModel):
    # Define a class attribute named text of type str
    text : str

# Define global variables for the model, vectorizer, and preprocessor
# Hint: model = None, vectorizer = None, preprocessor = TextPreprocessor()
model = None
vectorizer = None
preprocessor = TextPreprocessor()
# Define the startup event using the decorator @app.on_event("startup")
@app.on_event("startup")
# Define an async function named load_models
async def load_model():
    
    # Declare model and vectorizer as global variables
    # Hint: global model, vectorizer
    global model , vectorizer
    
    # Load the saved model from 'model.joblib' using joblib.load and assign it to the global model
    model = joblib.load('model.joblib')
    
    # Load the saved vectorizer from 'vectorizer.joblib' using joblib.load and assign it to the global vectorizer
    vectorizer = joblib.load('vectorizer.joblib')

# Define a POST endpoint using the decorator @app.post("/analyze")
@app.post("/analyze")
# Define an async function named analyze_sentiment that takes a parameter named request of type FeedbackRequest
async def analyze_sentiment(request:FeedbackRequest):
    
    # Extract the text from the request and store it in a variable named raw_text
    raw_text = request.text
    
    # Hint: raw_text = request.text
    
    # Clean the raw_text using the preprocess method of the preprocessor, store in clean_text
    clean_text = preprocessor.preprocess(raw_text)
    
    # Transform the clean_text into a list (e.g., [clean_text]) using the vectorizer's transform method, store in vectorized_text
    vectorized_text = vectorizer.transform([clean_text])
    
    # Predict the sentiment using the model's predict method on vectorized_text, store the first element [0] in prediction
    # Hint: prediction = model.predict(vectorized_text)[0]
    prediction = model.predict(vectorized_text)[0]
    
    # Get the confidence probabilities using the model's predict_proba method on vectorized_text, store the first element [0] in probabilities
    probabilities = model.predict_proba(vectorized_text)[0]
    # Hint: probabilities = model.predict_proba(vectorized_text)[0]
    
    # Find the maximum probability from the probabilities array using the max() function, store in confidence_score
    confidence_score = max(probabilities)

    
    # Return a dictionary containing "text": raw_text, "sentiment": prediction, and "confidence_score": float(confidence_score)
    return {
        "text" : raw_text,
        "sentiment" : prediction,
        "confidence_score": float(confidence_score)

    }