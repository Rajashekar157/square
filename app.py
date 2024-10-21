import streamlit as st

# Title of the app
st.title("Square Calculator")

# User input
number = st.number_input("Enter a number:", value=0)

# Calculate the square
square = number ** 2

# Display the result
st.write(f"The square of {number} is {square}.")