# Import json library
import json

# Import train_test_split from sklearn
from sklearn.model_selection import train_test_split

# Import classification_report and accuracy_score
from sklearn.metrics import classification_report, accuracy_score

# Import joblib for model serialization
import joblib

# Import custom pipeline modules
from data_loader import DataLoader
from text_preprocessor import TextPreprocessor
from feature_extractor import FeatureExtractor
from model_builder import ModelBuilder

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Initialize DataLoader with dataset path from config
data_loader = DataLoader(file_path=config['dataset_path'])
raw_dataframe = data_loader.load_data()

# Initialize TextPreprocessor
text_preprocessor = TextPreprocessor()

# Extract and clean feature column dynamically
raw_texts = raw_dataframe[config['text_column']]
clean_texts = [text_preprocessor.preprocess(text) for text in raw_texts]

# Extract target labels dynamically
target_labels = raw_dataframe[config['target_column']]

# Split dataset into training and testing sets
X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    clean_texts,
    target_labels,
    test_size=config['test_size'],
    random_state=config['random_state']
)

# Initialize and fit FeatureExtractor
feature_extractor = FeatureExtractor()
X_train_vectorized = feature_extractor.fit_transform(X_train_raw)
X_test_vectorized = feature_extractor.transform(X_test_raw)

# Initialize and train ModelBuilder
model_builder = ModelBuilder()
model_builder.train(X_train_vectorized, y_train)

# Evaluate model performance
y_pred = model_builder.predict(X_test_vectorized)
print("--- Model Accuracy ---")
print(accuracy_score(y_test, y_pred))
print("--- Classification Report ---")
print(classification_report(y_test, y_pred))

# Save trained model and vectorizer artifacts
model_builder.save_model('model.joblib')
feature_extractor.save_vectorizer('vectorizer.joblib')
print("Artifacts saved successfully!")