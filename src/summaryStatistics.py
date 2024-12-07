import pandas as pd

# List of individual CSV file paths
csv_files = [
    r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv', 
    r'C:\Users\hp\Documents\data\benin-malanville.csv',
    r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
]

# Function to calculate summary statistics for a given dataframe
def calculate_summary_statistics(df):
    return df.describe(include='all').transpose()

# Load the CSV files and compute statistics
for file in csv_files:
    df = pd.read_csv(file)
    
    # Calculate and display summary statistics
    print(f"Summary Statistics for {file}:\n")
    print(calculate_summary_statistics(df))
    print("\n" + "-"*50 + "\n")
