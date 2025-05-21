import pandas as pd

def clean_data(path):
    try:    
        # Load the dataset from the CSV file
        df = pd.read_csv(path)

        # Drop any rows with missing values (optional)
        df = df.dropna()

        return df
    except Exception as e:
        print("Error loading CSV:", e)
        return None