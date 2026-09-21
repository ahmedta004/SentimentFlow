from fastapi.testclient import TestClient
from main import app

def test_sentiment_endpoint(): 
    with TestClient(app) as client:
     response = client.post("/analyze", json= {"text": " I hate this product!"})
     assert response.status_code == 200
     assert response.json().get("sentiment") == "negative"