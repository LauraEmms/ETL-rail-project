import streamlit as st
import pandas as pd

# Load the processed data
df = pd.read_csv("output/2026-05-06_region_and_route.csv")

# Set page title
st.title("Railway Performance Dashboard")

# Display entire dataframe
st.write("Full Processed Dataset")
st.dataframe(df)

# Sidebar configuration
st.sidebar.header("Filter")

# Feature selection - numeric columns only
numeric_columns = df.select_dtypes(include="number").columns

selection = st.sidebar.selectbox(
    "Select a feature to visualise", 
    numeric_columns
)

# Range selection based on selected feature
min_value = float(df[selection].min())
max_value = float(df[selection].max())

range_slider = st.sidebar.slider(
    f"Select range for {selection}", 
    min_value, 
    max_value, 
    (min_value, max_value)
)

# Filter the dataframe based on range selected
filtered_df = df[df[selection].between(range_slider[0], range_slider[1])]

# Display filtered dataset
st.write(f"Filtered dataset for {selection}")
st.dataframe(filtered_df)

# Stats as visual cards rounded to 2 decimal places
col1, col2, col3 = st.columns(3)

col1.metric(f"Mean {selection}", round(filtered_df[selection].mean(), 2))
col2.metric(f"Median {selection}", round(filtered_df[selection].median(), 2))
col3.metric(f"Max {selection}", round(filtered_df[selection].max(), 2))

# Get index of max and min values for selection
max_idx = filtered_df[selection].idxmax()
min_idx = filtered_df[selection].idxmin()

# Extract full rows
max_row = filtered_df.loc[max_idx]
min_row = filtered_df.loc[min_idx]

# Assign column names
route_col = "network rail route"
region_col = "network rail region"

# Get route and region for max and min values
max_route = max_row[route_col]
max_region = max_row[region_col]

min_route = min_row[route_col]
min_region = min_row[region_col]

# Display extremes for selection 
st.subheader("Extremes")

st.write(f"#### Highest record for {selection}")
st.write(f"**Route**: {max_route}")
st.write(f"**Region**: {max_region}")

st.write(f"#### Lowest record for {selection}")
st.write(f"**Route**: {min_route}")
st.write(f"**Region**: {min_region}")