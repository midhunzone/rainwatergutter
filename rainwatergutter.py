import streamlit as st
import math

# Function to calculate pipe diameter
def calculate_pipe_diameter(area_sqft, rainfall_inches_per_hour, velocity_fps):
    # Convert area to square inches
    area_sqin = area_sqft * 144
    
    # Calculate runoff volume in cubic inches per hour
    runoff_cuin_per_hour = area_sqin * rainfall_inches_per_hour * 0.85
    
    # Convert runoff volume to cubic feet per hour
    runoff_cuft_per_hour = runoff_cuin_per_hour / 1728
    
    # Convert flow rate to cubic feet per second
    flow_rate_cuft_per_second = runoff_cuft_per_hour / 3600
    
    # Calculate pipe diameter using the formula
    diameter_feet = math.sqrt((4 * flow_rate_cuft_per_second) / (math.pi * velocity_fps))
    
    # Convert diameter to inches
    diameter_inches = diameter_feet * 12
    
    return diameter_inches

# Streamlit user interface
st.title("Pipe Size Estimation for Rainwater Gutter")

# User inputs
area_sqft = st.slider("Area to be serviced (sq ft)", min_value=100, max_value=5000, value=1000, step=10)
rainfall_inches_per_hour = st.slider("Rainfall rate (inches per hour)", min_value=1.0, max_value=10.0, value=8.0, step=0.1)
velocity_fps = st.slider("Water velocity in pipe (feet per second)", min_value=1.0, max_value=10.0, value=3.0, step=0.1)

# Calculate pipe diameter
pipe_diameter = calculate_pipe_diameter(area_sqft, rainfall_inches_per_hour, velocity_fps)

# Display the result
st.write(f"The required pipe diameter is **{pipe_diameter:.2f} inches**.")

