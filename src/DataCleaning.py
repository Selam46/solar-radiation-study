import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
csv_files = [
    r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv',
    r'C:\Users\hp\Documents\data\benin-malanville.csv',
    r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
]

def z_score_analysis(df, file_name):
    """Identify anomalies using Z-score method."""
    # Calculate Z-scores for numerical columns
    z_scores = np.abs(stats.zscore(df.select_dtypes(include=['float64', 'int64'])))
    
    # Define a threshold for identifying outliers (commonly 3)
    threshold = 3
    
    # Identify anomalies
    anomalies = (z_scores > threshold).any(axis=1)
    
    return anomalies

# Function for data cleaning
def clean_data(df, file_name):
    print(f"Data Cleaning for {file_name}:\n")
    
    # Drop entirely null columns like "Comments"
    if 'Comments' in df.columns:
        df = df.drop(columns=['Comments'])
    
    # Fill missing values in numerical columns with median
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = df[col].fillna(df[col].median())
    
    # Remove rows flagged as anomalies
    anomalies = z_score_analysis(df, file_name)
    df = df[~anomalies]
    
    print(f"Cleaned dataset saved as cleaned_{file_name}")
    df.to_csv(f"cleaned_{file_name}", index=False)

# Apply data cleaning
for file in csv_files:
    file_name = file.split("\\")[-1]
    df = pd.read_csv(file)
    clean_data(df, file_name)
