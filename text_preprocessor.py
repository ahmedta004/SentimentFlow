# Import the regular expressions module
import re

# Import the string module for punctuation handling
import string

# Import the nltk library
import nltk

# Import stopwords from nltk.corpus
from nltk.corpus import stopwords

# Import PorterStemmer from nltk.stem
from nltk.stem import PorterStemmer

# Download the stopwords dataset quietly
nltk.download('stopwords', quiet=True)

# Define the text preprocessing class named TextPreprocessor
class TextPreprocessor:

    # Initialize the class
    def __init__(self):
        
        # Initialize the PorterStemmer with parentheses and store it in self.stemmer
        self.stemmer = PorterStemmer()
        
        # Retrieve the English stopwords list, convert it to a Python set, and store it in self.stop_words
        self.stop_words = set(stopwords.words('english'))

    # Define a method named remove_urls that takes self and text
    def remove_urls(self, text):
        # Use re.sub to replace the regex pattern r'http\S+' with an empty string
        clean_text = re.sub(r'http\S+', '', text)
        # Return the cleaned text
        return clean_text

    # Define a method named remove_mentions that takes self and text
    def remove_mentions(self, text):
        # Use re.sub to replace the regex pattern r'@\w+' with an empty string
        clean_text = re.sub(r'@\w+', '', text)
        # Return the cleaned text
        return clean_text

    # Define a method named clean_whitespace that takes self and text
    def clean_whitespace(self, text):
        # Use re.sub to replace multiple whitespace characters with a single space
        clean_text = re.sub(r'\s+', ' ', text)
        # Use the strip method to remove leading and trailing spaces
        clean_text = clean_text.strip()
        # Return the cleaned text
        return clean_text

    # Define a method named to_lowercase that takes self and text
    def to_lowercase(self, text):
        # Convert the text to lowercase using the lower method and return it
        return text.lower()
        
    # Define a method named remove_punctuation that takes self and text
    def remove_punctuation(self, text):
        # Create a translation table to map punctuation to empty strings
        translation_table = str.maketrans('', '', string.punctuation)
        
        # Translate the text using the table and return it
        return text.translate(translation_table)
        
    # Define a method named remove_stopwords that takes self and text
    def remove_stopwords(self, text):
        # Split the text string into a list of words using split method
        words_list = text.split()
        
        # Create a new list for words that are not in self.stop_words using list comprehension
        filtered_words = [word for word in words_list if word not in self.stop_words]
        
        # Join the filtered words back into a single string separated by spaces and return it
        return " ".join(filtered_words)
        
    # Define a method named apply_stemming that takes self and text
    def apply_stemming(self, text):
        # Split the text string into a list of words
        words_list = text.split()
        
        # Apply self.stemmer.stem to each word in the list using list comprehension
        stemmed_words = [self.stemmer.stem(word) for word in words_list]
        
        # Join the stemmed words back into a single string separated by spaces and return it
        return " ".join(stemmed_words)
    # Define a method named preprocess that takes self and text
    def preprocess(self,text):

    
        # Call self.to_lowercase passing text, and assign the result back to text
        text = self.to_lowercase(text)
        
        # Call self.remove_urls passing text, and assign the result back to text
        text = self.remove_urls(text)
        
        # Call self.remove_mentions passing text, and assign the result back to text
        text = self.remove_mentions(text)
        
        # Call self.remove_punctuation passing text, and assign the result back to text
        text = self.remove_punctuation(text)
        # Call self.clean_whitespace passing text, and assign the result back to text
        text = self.clean_whitespace(text)
        # Call self.remove_stopwords passing text, and assign the result back to text
        text = self.remove_stopwords(text)
        # Call self.apply_stemming passing text, and assign the result back to text
        text= self.apply_stemming(text)
        # Return the final cleaned text
        return text

