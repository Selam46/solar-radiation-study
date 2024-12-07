import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
csv_files = [
    r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv',
    r'C:\Users\hp\Documents\data\benin-malanville.csv',
    r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
]

# Function to create bubble charts
def bubble_chart(df, file_name):
    print(f"Bubble Chart for {file_name}:\n")
    
    if 'GHI' in df.columns and 'Tamb' in df.columns and 'WS' in df.columns and 'RH' in df.columns:
        plt.figure(figsize=(8, 5))
        plt.scatter(df['GHI'], df['Tamb'], s=df['WS']*10, alpha=0.6, c=df['RH'], cmap='viridis')
        plt.colorbar(label='Relative Humidity (RH)')
        plt.title(f"Bubble Chart - GHI vs. Tamb vs. WS ({file_name})")
        plt.xlabel("Global Horizontal Irradiance (GHI)")
        plt.ylabel("Temperature (Tamb)")
        plt.grid(True)
        plt.show()

# Apply bubble charts
for file in csv_files:
    file_name = file.split("\\")[-1]
    df = pd.read_csv(file)
    bubble_chart(df, file_name)
