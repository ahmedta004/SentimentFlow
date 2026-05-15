# Import the pandas library and alias it as pd
import pandas as pd

# Define the DataLoader class for data ingestion
class DataLoader:

    # Initialize the class with a constructor that takes self and file_path
    def __init__(self,file_path):
    
        # Assign the passed file_path to an instance variable named self.file_path
        self.file_path = file_path
        
    # Define a method named load_data that takes self
    def load_data(self):
    
        # Start a try block to handle potential file errors
        try:
         
            # Use pandas to read the CSV file from self.file_path and store it in a variable named df
            df = pd.read_csv(self.file_path)
            # Return the dataframe df
            return df
            
        # Start an except block specifically for FileNotFoundError
        except FileNotFoundError :
            # Print an error message stating the file was not found
            print("Erro: File is not founded!")
            # Return None to indicate failure safely
            return None
        

# Check if the script is being run directly
if __name__ == '__main__':
    
    # Create an instance of DataLoader with a fake file path like "fake_dataset.csv"
    data_loader = DataLoader("fake_dataset.csv")
    # Call the load_data method on the instance and store the result in a variable named data
    data = data_loader.load_data()
    # Print the data variable to the console
    print(data)