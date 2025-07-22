import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄")

st.title("Unit Converter")

conversion = st.selectbox("Choose a conversion type", [
    "Kilometers to Miles",
    "Miles to Kilometers",
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Kilograms to Pounds",
    "Pounds to Kilograms"
])

value = st.number_input("Enter value:", value=0.0)

if st.button("Convert"):
    if conversion == "Kilometers to Miles":
        result = value * 0.621371
    elif conversion == "Miles to Kilometers":
        result = value / 0.621371
    elif conversion == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
    elif conversion == "Fahrenheit to Celsius":
        result = (value - 32) * 5/9
    elif conversion == "Kilograms to Pounds":
        result = value * 2.20462
    elif conversion == "Pounds to Kilograms":
        result = value / 2.20462

    st.success(f"Converted Value: {result}")
