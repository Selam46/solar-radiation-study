from windrose import WindroseAxes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
csv_files = [
    r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv',
    r'C:\Users\hp\Documents\data\benin-malanville.csv',
    r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
]
# Function to create wind rose plots
def wind_analysis(df, file_name):
    print(f"Wind Analysis for {file_name}:\n")
    
    if 'WS' in df.columns and 'WD' in df.columns:
        # Create a wind rose plot
        ax = WindroseAxes.from_ax()
        ax.bar(df['WD'], df['WS'], normed=True, opening=0.8, edgecolor='white')
        ax.set_title(f"Wind Rose - {file_name}")
        ax.set_legend()
        plt.show()

# Apply wind analysis
for file in csv_files:
    file_name = file.split("\\")[-1]
    df = pd.read_csv(file)
    wind_analysis(df, file_name)
