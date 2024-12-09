# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats
# import seaborn as sns
# csv_files = [
#     r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv',
#     r'C:\Users\hp\Documents\data\benin-malanville.csv',
#     r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
# ]

# def z_score_analysis(df, file_name):
#     """Identify anomalies using Z-score method."""
#     # Calculate Z-scores for numerical columns
#     z_scores = np.abs(stats.zscore(df.select_dtypes(include=['float64', 'int64'])))
    
#     # Define a threshold for identifying outliers (commonly 3)
#     threshold = 3
    
#     # Identify anomalies
#     anomalies = (z_scores > threshold).any(axis=1)
    
#     return anomalies

# # Function for data cleaning
# def clean_data(df, file_name):
#     print(f"Data Cleaning for {file_name}:\n")
    
#     # Drop entirely null columns like "Comments"
#     if 'Comments' in df.columns:
#         df = df.drop(columns=['Comments'])
    
#     # Fill missing values in numerical columns with median
#     for col in df.select_dtypes(include=['float64', 'int64']).columns:
#         df[col] = df[col].fillna(df[col].median())
    
#     # Remove rows flagged as anomalies
#     anomalies = z_score_analysis(df, file_name)
#     df = df[~anomalies]
    
#     print(f"Cleaned dataset saved as cleaned_{file_name}")
#     df.to_csv(f"cleaned_{file_name}", index=False)

# # Apply data cleaning
# for file in csv_files:
#     file_name = file.split("\\")[-1]
#     df = pd.read_csv(file)
#     clean_data(df, file_name)









import os
import numpy as np
import pandas as pd
from scipy import stats

# List of CSV files directly
csv_files = [
    r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv',
    r'C:\Users\hp\Documents\data\benin-malanville.csv',
    r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
]

def z_score_analysis(df):
    """Identify anomalies in the dataset using the Z-score method."""
    try:
        z_scores = np.abs(stats.zscore(df.select_dtypes(include=['float64', 'int64'])))
        threshold = 3  # Common threshold for outliers
        return (z_scores > threshold).any(axis=1)
    except Exception as e:
        print(f"Error in Z-score analysis: {e}")
        return pd.Series([False] * len(df))

def clean_data(df):
    """Clean the input DataFrame by handling missing values and removing anomalies."""
    try:
        if 'Comments' in df.columns:
            df = df.drop(columns=['Comments'])
        
        # Fill missing values in numerical columns with the median
        for col in df.select_dtypes(include=['float64', 'int64']).columns:
            df[col] = df[col].fillna(df[col].median())
        
        # Remove rows flagged as anomalies
        anomalies = z_score_analysis(df)
        return df[~anomalies]
    except Exception as e:
        print(f"Error during data cleaning: {e}")
        return df

def process_files(csv_files, output_dir):
    """Process the CSV files, clean them, and save to the output directory."""
    try:
        os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
        for file_path in csv_files:
            if file_path.endswith('.csv'):
                file_name = os.path.basename(file_path)  # Get the file name from the path
                df = pd.read_csv(file_path)  # Read the actual CSV file
                cleaned_df = clean_data(df)
                cleaned_file_path = os.path.join(output_dir, f"cleaned_{file_name}")
                cleaned_df.to_csv(cleaned_file_path, index=False)
                print(f"Cleaned data saved to {cleaned_file_path}")
    except Exception as e:
        print(f"Error processing files: {e}")

if __name__ == "__main__":
    output_directory = r"C:\Users\hp\solar-radiation-study\data"  # Path to save cleaned files
    process_files(csv_files, output_directory)