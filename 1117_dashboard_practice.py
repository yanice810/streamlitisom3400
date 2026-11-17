import streamlit as st

# Title and Header
st.title("Reatail Business Dashboard")
st.head("Manager Input Section")

# Instruction
st.write("Please enter the monthly sales target and select the region.")


# Number input for sales target
sales = st.number_input("Enter Monthly Sales Target(in USD):",
                      min_value=0,
                      max_value=120,
                      value=25)
st.write(sales)



# Dropdown for region selection



# Submit button
if st.button("Submit"):
    # Display entered values



    # Success message



    # Extra message for ambitious target




