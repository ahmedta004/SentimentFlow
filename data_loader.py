# Import the pandas library and alias it as pd
import pandas as pd

# Define the DataLoader class for data ingestion
class DataLoader:

    # Initialize the class with a constructor that takes self and file_path
    
        # Assign the passed file_path to an instance variable named self.file_path
        
    # Define a method named load_data that takes self
    
        # Start a try block to handle potential file errors
        
            # Use pandas to read the CSV file from self.file_path and store it in a variable named df
            
            # Return the dataframe df
            
        # Start an except block specifically for FileNotFoundError
        
            # Print an error message stating the file was not found
            
            # Return None to indicate failure safely