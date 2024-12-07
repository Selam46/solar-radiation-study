import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

csv_files = [
    r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv',
    r'C:\Users\hp\Documents\data\benin-malanville.csv',
    r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
]


# Function to calculate Z-scores
def z_score_analysis(df, file_name):
    print(f"Z-Score Analysis for {file_name}:\n")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    z_scores = df[numeric_cols].apply(zscore)
    anomalies = (z_scores.abs() > 3).any(axis=1)  # Flag anomalies where Z-score > 3
    
    print(f"Number of Anomalies Detected: {anomalies.sum()}\n")
    return anomalies

# Apply Z-score analysis
for file in csv_files:
    file_name = file.split("\\")[-1]
    df = pd.read_csv(file)
    anomalies = z_score_analysis(df, file_name)
    # Optionally, save flagged rows
    df[anomalies].to_csv(f"anomalies_{file_name}", index=False)
