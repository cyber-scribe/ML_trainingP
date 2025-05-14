import streamlit as st
import pickle
st.title("Price Predictor App")

A = st.number_input("Enter the Population:")
B = st.number_input("Enter the Monthly Income:")
C = st.number_input("Enter the Average Parking Per Month:")
D = st.number_input("Enter the Number of Weekly Riders:")

button =st.button("Predict the Taxi Price per Week!!")

if(button):
    model=pickle.load(open("mod.pkl","rb"))
    res = model.predict([[A,B,C,D]])[0]
    st.markdown(f"Predicted Taxi Price per Weeek is: {res}")