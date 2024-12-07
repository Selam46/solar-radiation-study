import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data function with caching to optimize performance
@st.cache
def load_data():
    return pd.read_csv(r"C:\Users\hp\Documents\data\togo-dapaong_qc.csv")
  # Adjust path to your dataset

# Function to display the Streamlit dashboard
def main():
    st.title("Solar Radiation Study Dashboard")
    st.sidebar.title("Navigation")
    
    options = st.sidebar.radio("Select a Page:", ["Overview", "Analysis", "Data Cleaning"])

    # Load the dataset
    data = load_data()

    if options == "Overview":
        st.subheader("Dataset Overview")
        st.write(data.head())  # Show the first few rows of the dataset
        st.write("### Basic Statistics")
        st.write(data.describe())  # Show basic statistics of the dataset

    elif options == "Analysis":
        st.subheader("Data Visualization")
        
        # Add interactive feature to choose which column to plot
        column = st.selectbox("Select a variable to plot:", data.columns)
        plot_type = st.radio("Plot Type:", ["Histogram", "Time Series"])

        # Display Histogram or Time Series plot
        if plot_type == "Histogram":
            fig, ax = plt.subplots()
            sns.histplot(data[column], kde=True, ax=ax)
            st.pyplot(fig)

        elif plot_type == "Time Series":
            if "Date" in data.columns:
                data["Date"] = pd.to_datetime(data["Date"])  # Ensure the 'Date' column is in datetime format
                fig, ax = plt.subplots()
                data.plot(x="Date", y=column, ax=ax)
                st.pyplot(fig)
            else:
                st.error("The dataset does not have a 'Date' column.")

        # **Interactive Feature: Wind Speed Filter (Slider)**
        st.write("### Filter Data by Wind Speed")
        wind_speed = st.slider("Select Wind Speed Range:", 0, 20, (5, 15))  # Slider to filter by wind speed
        filtered_data = data[(data['WS'] >= wind_speed[0]) & (data['WS'] <= wind_speed[1])]
        st.write(filtered_data)  # Display filtered data

        # **Interactive Feature: File Upload (Custom Dataset)**
        st.write("### Upload Your Own Dataset")
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
        if uploaded_file:
            uploaded_data = pd.read_csv(uploaded_file)  # Read the uploaded CSV file
            st.write("Uploaded Dataset:")
            st.write(uploaded_data.head())  # Show the first few rows of the uploaded data

    elif options == "Data Cleaning":
        st.subheader("Data Cleaning Options")
        st.write("Implement data cleaning functionalities here (e.g., handle missing values).")

if __name__ == "__main__":
    main()
