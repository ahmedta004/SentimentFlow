# Import the regular expressions module
import re

# Define the text preprocessing class named TextPreprocessor
class TextPreprocessor:

    # Initialize the class with an empty constructor
    def __init__(self):
        pass

    # Define a method named remove_urls that takes self and text as parameters
    def remove_urls (self,text):

        # Use re.sub to replace the regex pattern r'http\S+' with an empty string '' in the text
        clean_text = re.sub(r'http\S+', '',text)
        # Return the cleaned text string
        return clean_text
# Define a method named remove_mentions that takes self and text
    def remove_mentions(self,text):

        # Use re.sub to replace the regex pattern r'@\w+' with an empty string ''
        clean_text = re.sub(r'@\w+', '', text)
        # Return the cleaned text string
        return clean_text
    


    # Define a method named clean_whitespace that takes self and text
    def clean_whitespace(self,text):
        
        # Use re.sub to replace multiple whitespace characters r'\s+' with a single space ' '
        clean_text = re.sub(r'\s+',' ',text)
        # Use the strip method on the result to remove leading and trailing spaces
        clean_text = clean_text.strip()
        # Return the fully cleaned text string
        return clean_text



# Check if the script is being run directly
if __name__ == '__main__':

    # Create a sample tweet variable containing a URL and a mention
    my_tweet = "@VirginAmerica my flight is delayed! check https://example.com"
    # Example: "@VirginAmerica my flight is delayed! check https://example.com"
    
    # Instantiate the TextPreprocessor class and store it in an object named processor
    processor = TextPreprocessor()
    # Call remove_urls on the sample tweet and store the result in a new variable
    cleaned_tweet = processor.remove_urls(my_tweet)
    # Call remove_mentions on the result from the previous step and update the variable
    cleaned_tweet = processor.remove_mentions(cleaned_tweet)\
    #call remove_whitespace
    cleaned_tweet = processor.clean_whitespace(cleaned_tweet)
    # Print the final cleaned text to the console to verify the output
    print(cleaned_tweet)