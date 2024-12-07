import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# List of individual CSV file paths
csv_files = [
    r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv',
    r'C:\Users\hp\Documents\data\benin-malanville.csv',
    r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
]

# Function to plot time series data
def time_series_analysis(df, file_name):
    print(f"Time Series Analysis for {file_name}:\n")
    
    # Ensure a datetime column is present
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.set_index('Timestamp', inplace=True)
    
    # Plot GHI, DNI, DHI, and Tamb over time
    for col in ['GHI', 'DNI', 'DHI', 'Tamb']:
        if col in df.columns:
            plt.figure(figsize=(10, 5))
            sns.lineplot(data=df, x=df.index, y=col)
            plt.title(f"{col} Over Time ({file_name})")
            plt.xlabel("Time")
            plt.ylabel(col)
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.show()
    
    # Evaluate the impact of cleaning on sensor readings (ModA, ModB)
    if 'Cleaning' in df.columns and 'ModA' in df.columns and 'ModB' in df.columns:
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=df, x=df.index, y='ModA', label='ModA - Original')
        sns.lineplot(data=df[df['Cleaning'] == 1], x=df[df['Cleaning'] == 1].index, y='ModA', label='ModA - Cleaned')
        plt.title(f"Impact of Cleaning on ModA ({file_name})")
        plt.xlabel("Time")
        plt.ylabel("ModA")
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()
        
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=df, x=df.index, y='ModB', label='ModB - Original')
        sns.lineplot(data=df[df['Cleaning'] == 1], x=df[df['Cleaning'] == 1].index, y='ModB', label='ModB - Cleaned')
        plt.title(f"Impact of Cleaning on ModB ({file_name})")
        plt.xlabel("Time")
        plt.ylabel("ModB")
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

# Apply time series analysis on all files
for file in csv_files:
    file_name = file.split("\\")[-1]
    df = pd.read_csv(file)
    time_series_analysis(df, file_name)
