import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# List of individual CSV file paths
csv_files = [
    r'C:\Users\hp\Documents\data\togo-dapaong_qc.csv',
    r'C:\Users\hp\Documents\data\benin-malanville.csv',
    r'C:\Users\hp\Documents\data\sierraleone-bumbuna.csv'
]

# Function for correlation analysis
def correlation_analysis(df, file_name):
    print(f"Correlation Analysis for {file_name}:\n")
    
    # Calculate correlation matrix for solar radiation and temperature measures
    relevant_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD']
    available_columns = [col for col in relevant_columns if col in df.columns]
    
    if available_columns:
        corr_matrix = df[available_columns].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title(f"Correlation Matrix - {file_name}")
        plt.show()

    # Pair plots for solar radiation and wind conditions
    if set(['GHI', 'DNI', 'DHI', 'WS', 'WSgust']).issubset(df.columns):
        sns.pairplot(df[['GHI', 'DNI', 'DHI', 'WS', 'WSgust']])
        plt.suptitle(f"Pair Plot - {file_name}")
        plt.show()

# Apply correlation analysis
for file in csv_files:
    file_name = file.split("\\")[-1]
    df = pd.read_csv(file)
    correlation_analysis(df, file_name)
