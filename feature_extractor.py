# Import TfidfVectorizer from sklearn.feature_extraction.text
from sklearn.feature_extraction.text import TfidfVectorizer
# Define the FeatureExtractor class
class FeatureExtractor:


    # Initialize the class with a constructor that takes self and max_features set to 5000 by default
    def __init__(self,max_features = 5000):
    
        # Instantiate TfidfVectorizer with max_features parameter and store it in self.vectorizer
        self.vectorizer = TfidfVectorizer(max_features=max_features)
        
    # Define a method named fit_transform that takes self and texts
    def fit_transform(self,texts):
    
        # Call fit_transform on self.vectorizer using the texts list and store the result in a matrix variable
        matrix = self.vectorizer.fit_transform(texts)

        
        # Return the resulting matrix
        return matrix
        
    # Define a method named transform that takes self and texts
    def transform(self,texts):
    
        # Call transform on self.vectorizer using the texts list and store the result in a matrix variable
        matrix = self.vectorizer.transform(texts)
        
        # Return the resulting matrix
        return matrix
    
# Check if the script is being run directly
if __name__ == '__main__':
    
    # Create an instance of the FeatureExtractor
    extractor = FeatureExtractor()
    
    # Create a dummy list of training texts
    train_texts = ["I love my delayed flight", "worst service ever", "flight was super delayed"]
    
    # Call fit_transform on the extractor using train_texts and store in train_matrix
    train_matrix = extractor.fit_transform(train_texts)
    # Print the shape of the train_matrix (Hint: print(train_matrix.shape))
    print(train_matrix.shape)

    
    # Create a dummy list for a new unseen tweet
    new_tweet = ["I am angry about the flight"]
    
    # Call transform ONLY on the extractor using new_tweet and store in new_matrix
    new_matrix = extractor.transform(new_tweet)

    
    # Print the shape of the new_matrix
    print(new_matrix.shape)