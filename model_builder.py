# Import LogisticRegression from sklearn.linear_model
from sklearn.linear_model import LogisticRegression

# Import accuracy_score and classification_report from sklearn.metrics
from sklearn.metrics import accuracy_score , classification_report

# Define the ModelBuilder class
class ModelBuilder:

    # Initialize the class with an empty constructor
    def __init__(self):
    
        # Instantiate LogisticRegression with max_iter set to 1000 and store it in self.model
        self.model = LogisticRegression(max_iter=1000)
        
    # Define a method named train that takes self, X_train, and y_train
    def train(self,x_trian,y_train):
    
        # Call fit on self.model using X_train and y_train
        self.model.fit(x_trian,y_train)

        
    # Define a method named predict that takes self and X
    def predict(self,x):
    
        # Call predict on self.model using X and return the predictions
        return self.model.predict(x)
        
    # Define a method named evaluate that takes self, y_true, and y_pred
    def evaluate(self,y_true,y_pred):
    
        # Calculate the accuracy using accuracy_score with y_true and y_pred, and store it
        accuracy = accuracy_score(y_true,y_pred)
        
        # Generate the classification report using classification_report with y_true and y_pred, and store it
        report = classification_report(y_true,y_pred)
        
        # Print a formatted string or separator for the accuracy
        print("--- Model Accuracy ---")
        # Print the accuracy variable
        print(accuracy)
        
        # Print a formatted string or separator for the classification report
        print("--- Classification Report ---")
        # Print the classification report variable
        print(report)