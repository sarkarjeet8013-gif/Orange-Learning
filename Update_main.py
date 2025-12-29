import streamlit as st

st.title("Interactive Streamlit App")

name=st.type_title("Enter your Name: ")
if st.button("Submit"):
  st.write("Hello!", name, "Welcome to Streamlit")
