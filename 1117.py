import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# -------------------------------
# Title and Description
# -------------------------------
st.title("📊 Business Sales Dashboard")
st.write("Analyze monthly sales data interactively!")

# -------------------------------
# Sample Data
# -------------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]  #create the dictionary, story in the data, the data frame
sales = np.random.randint(5000, 20000, size=12)  #random generated, generate the number randomly, 5000 and 20000 range, generate 12 numbers
expenses = np.random.randint(3000, 15000, size=12)

data = pd.DataFrame({
    "Month": months,
    "Sales": sales,
    "Expenses": expenses
})

#because does not use the st., so will not show/see anything
# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("Filters")  #sidebar have multi selection
selected_months = st.sidebar.multiselect("Select Months", months,
                                         default=months)
show_expenses = st.sidebar.checkbox("Show Expenses", value=True)

# Filter data
filtered_data = data[data["Month"].isin(selected_months)]
