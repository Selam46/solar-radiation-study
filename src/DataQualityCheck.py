import pandas as pd

# List of individual CSV file paths
csv_files = [
    r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv',
    r'C:\Users\hp\Documents\data\benin-malanville.csv',
    r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
]

# Function to perform data quality checks
def data_quality_check(df, file_name):
    print(f"Data Quality Check for {file_name}:\n")
    
    # Check for missing values
    missing_values = df.isnull().sum()
    print(f"Missing Values:\n{missing_values}\n")
    
    # Check for negative values in GHI, DNI, DHI
    for col in ['GHI', 'DNI', 'DHI']:
        if col in df.columns:
            negative_count = (df[col] < 0).sum()
            print(f"Negative Values in {col}: {negative_count}")
    
    # Check for outliers in sensor readings (ModA, ModB) and wind speed data (WS, WSgust)
    for col in ['ModA', 'ModB', 'WS', 'WSgust']:
        if col in df.columns:
            outliers = df[col][(df[col] < df[col].quantile(0.01)) | (df[col] > df[col].quantile(0.99))]
            print(f"Outliers in {col}: {len(outliers)}")
    print("\n" + "-"*50 + "\n")

# Apply data quality check on all files
for file in csv_files:
    file_name = file.split("\\")[-1]
    df = pd.read_csv(file)
    data_quality_check(df, file_name)
