# Import train_test_split from sklearn.model_selection
from sklearn.model_selection import train_test_split

# Import joblib
import joblib

# Import DataLoader from data_loader
from data_loader import DataLoader
# Import TextPreprocessor from text_preprocessor
from text_preprocessor import TextPreprocessor
# Import FeatureExtractor from feature_extractor
from feature_extractor import FeatureExtractor
# Import ModelBuilder from model_builder
from model_builder import ModelBuilder

# Check if the script is being run directly
if __name__ == '__main__':

    # --- 1. DATA INGESTION ---
    # Initialize DataLoader with your dataset path (e.g., 'dataset.csv')
    loader = DataLoader('tweets.csv')
    
    # Load the data and store it in a dataframe variable named df
    df = loader.load_data()
    
    # Extract the texts into a variable X and the labels into a variable y
    # Hint: X = df['text_column_name'], y = df['label_column_name']
    X = df['text']
    y = df['airline_sentiment']    
    # --- 2. DATA SPLITTING (Preventing Data Leakage) ---
    # Split X and y into X_train, X_test, y_train, y_test using train_test_split with test_size=0.2 and random_state=42
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # --- 3. TEXT PREPROCESSING ---
    # Initialize the TextPreprocessor
    preprocessor = TextPreprocessor()
    # Apply the preprocess method to each text in X_train using a list comprehension, store in X_train_clean
    X_train_clean = [preprocessor.preprocess(x) for x in X_train]
    
    # Apply the preprocess method to each text in X_test using a list comprehension, store in X_test_clean
    X_test_clean = [preprocessor.preprocess(x) for x in X_test]
    
    # --- 4. FEATURE EXTRACTION (VECTORIZATION) ---
    # Initialize the FeatureExtractor
    extractor = FeatureExtractor()
    
    # Call fit_transform on the extractor using X_train_clean and store in X_train_vec
    X_train_vec = extractor.fit_transform(X_train_clean)
    # Call transform ONLY on the extractor using X_test_clean and store in X_test_vec
    X_test_vec = extractor.transform(X_test_clean)
    
    # --- 5. MODEL TRAINING & EVALUATION ---
    # Initialize the ModelBuilder
    builder = ModelBuilder()
    
    # Call the train method on the model using X_train_vec and y_train
    builder.train(X_train_vec, y_train)
    
    # Call the predict method on the model using X_test_vec and store in y_pred
    y_pred = builder.predict(X_test_vec)
    
    # Call the evaluate method on the model using y_test and y_pred
    builder.evaluate(y_test,y_pred)
    
    # --- 6. SERIALIZATION (SAVING THE SYSTEM) ---
    # Save the trained LogisticRegression model to a file named 'model.joblib' using joblib.dump
    # Hint: joblib.dump(model_instance.model, 'model.joblib')
    joblib.dump(builder.model, 'model.joblib')
    
    # Save the fitted TfidfVectorizer to a file named 'vectorizer.joblib' using joblib.dump
    # Hint: joblib.dump(extractor_instance.vectorizer, 'vectorizer.joblib')
    joblib.dump(extractor.vectorizer,'vectorizer.joblib')
    
    # Print a success message indicating the training is complete and files are saved
    print("trained successfully! ")