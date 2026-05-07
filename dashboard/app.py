import streamlit as st
import pandas as pd
# import altair as alt

# Load the processed data
df = pd.read_csv("output/2026-05-06_region_and_route.csv")

# Set page title
st.title("Railway Performance Dashboard")

# Display entire dataframe
st.write("Full Processed Dataset")
st.dataframe(df)

# Sidebar configuration
st.sidebar.header("Filter")

# Feature selection 
feature = st.sidebar.selectbox(
    "Select a feature to visualise", 
    df.columns[[3,4,5,6,7]]
)

# Range selection based on selected feature
min_value = float(df[feature].min())
max_value = float(df[feature].max())

range_slider = st.sidebar.slider(
    f"Select range for {feature}", 
    min_value, 
    max_value, 
    (min_value, max_value)
)


