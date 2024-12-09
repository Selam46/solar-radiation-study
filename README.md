# Solar Radiation Study Project 
This repository contains the analysis and scripts for studying solar radiation and related environmental parameters. The project aims to explore, clean, and analyze datasets containing measurements such as solar radiation components (GHI, DNI, DHI), temperature, wind conditions, and relative humidity. These analyses help identify trends, correlations, and anomalies in solar radiation data, which can be critical for applications in renewable energy and climate studies.

## Streamlit Dashboard
The project includes a Streamlit dashboard to visualize and interact with the solar radiation dataset.

### Features
- Interactive histograms and time-series visualizations.
- Dataset overview and basic statistics.
- Filtering options for wind speed and other parameters.


## Set up Instructions 
Step 1: Clone the Repository

git clone https://github.com/Selam46/solar-radiation-study.git

cd solar-radiation-study

Step 2: Install Dependencies

Create a virtual environment and install required packages:

python3 -m venv venv

source venv/bin/activate    # On Windows: venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Step 3: Run Preprocessing Scripts

Run the preprocessing module to clean and prepare data:

python app/main.py