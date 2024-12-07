import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_files = [
    r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv',
    r'C:\Users\hp\Documents\data\benin-malanville.csv',
    r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
]

def plot_histograms(df, file_name):
    print(f"Histograms for {file_name}:\n")
    cols_to_plot = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb']
    for col in cols_to_plot:
        if col in df.columns:
            plt.figure(figsize=(8, 5))
            sns.histplot(df[col], kde=True, bins=30)
            plt.title(f"Histogram of {col} - {file_name}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.grid(True)
            plt.show()

# Apply histograms
for file in csv_files:
    file_name = file.split("\\")[-1]
    df = pd.read_csv(file)
    plot_histograms(df, file_name)
