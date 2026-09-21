# Import LogisticRegression from sklearn
from sklearn.linear_model import LogisticRegression

# Import metrics
from sklearn.metrics import accuracy_score, classification_report

# Import joblib
import joblib

# Define the ModelBuilder class
class ModelBuilder:

    # Initialize the class constructor
    def __init__(self):
        self.model = LogisticRegression(max_iter=1000)

    # Train the model on training set
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    # Predict outputs for new inputs
    def predict(self, X):
        return self.model.predict(X)

    # Save model artifact to disk
    def save_model(self, file_path):
        joblib.dump(self.model, file_path)

    # Evaluate performance on test data
    def evaluate(self, y_true, y_pred):
        accuracy = accuracy_score(y_true, y_pred)
        report = classification_report(y_true, y_pred)
        print("--- Model Accuracy ---")
        print(accuracy)
        print("--- Classification Report ---")
        print(report)