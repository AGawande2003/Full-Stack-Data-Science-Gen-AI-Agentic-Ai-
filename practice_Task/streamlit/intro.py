import streamlit as st
st.title("My first streamlit app Cerated by Adarsh Gawande")
st.write("Welcome ! THis app calculates the square of numbers ")
st.header("select a number")
number = st.slider("pick a number",0,0,100)
st.subheader("Result")
squared_number =number*number
st.write(f"the square root of {number} is {squared_number}.")
