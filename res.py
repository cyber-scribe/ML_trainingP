import streamlit as st
import pickle
st.title(" Score prediction App")

sh = st.number_input("Enter the number of Study hours:")

button =st.button("Predict the Score!!")
