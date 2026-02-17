import streamlit as st
st.write("### WELCOME TO MR_AARAV_YT'S MINI PROJECT")
import numpy as np
from model import train

# Title
st.title("Hello World AI App")
st.subheader("A Simple Regression Model")

# Train model
model = train()

# Sidebar
st.sidebar.header("Input Features")
input_values = st.sidebar.slider("Select value of X", 1, 10, 1)

# Prediction
input_array = np.array([[input_values]])
prediction = model.predict(input_array)

# Display result
st.write(f"## Input value: {input_values}")
st.write(f"## Output value: {prediction[0]:.2f}") 