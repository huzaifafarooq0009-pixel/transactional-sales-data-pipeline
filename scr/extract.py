# -----------------------------
# Extract Script for Sales Data
# -----------------------------
# Purpose:
# This script loads raw sales data from a CSV file into a pandas DataFrame.
# This is the "Extract" part of ETL (Extract, Transform, Load)
# -----------------------------

# Import the pandas library
# Pandas is used to read CSV files and manipulate tabular data
import pandas as pd

# Define a function to extract data
def extract_data(file_path):
    """
    Reads a CSV file and returns it as a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file

    Returns:
        pd.DataFrame: Data loaded from the CSV file
    """
    # Read the CSV file using pandas
    df = pd.read_csv(file_path)

    # Return the loaded data
    return df

# The following code runs only if this script is executed directly
# (It will not run if you import this file into another script)
if __name__ == "__main__":
    
    # Specify the file path to the raw CSV data
    # Make sure this path is correct relative to the project root folder
    csv_file_path = "data/raw/sales_raw.csv"
    
    # Call the extract_data function to read the CSV into a DataFrame
    df = extract_data(csv_file_path)
    
    # Print a message to show that extraction is successful
    print("Raw sales data loaded successfully!\n")
    
    # Print the first 5 rows of the data to verify it
    print("Preview of the raw data:")
    print(df.head())
    
    # Optional: print the shape of the data (rows x columns)
    print(f"\nTotal rows: {df.shape[0]}, Total columns: {df.shape[1]}")




