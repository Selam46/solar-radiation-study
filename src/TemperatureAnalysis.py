# Function for temperature and relative humidity analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
csv_files = [
    r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv',
    r'C:\Users\hp\Documents\data\benin-malanville.csv',
    r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
]
def temperature_analysis(df, file_name):
    print(f"Temperature Analysis for {file_name}:\n")
    
    if 'RH' in df.columns and 'Tamb' in df.columns:
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df['RH'], y=df['Tamb'])
        plt.title(f"Temperature vs. Relative Humidity - {file_name}")
        plt.xlabel("Relative Humidity (RH)")
        plt.ylabel("Temperature (Tamb)")
        plt.grid(True)
        plt.show()

# Apply temperature analysis
for file in csv_files:
    file_name = file.split("\\")[-1]
    df = pd.read_csv(file)
    temperature_analysis(df, file_name)
