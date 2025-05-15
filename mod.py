import streamlit as st
import pickle
st.title("Weekly Riders Prediction App")

A = st.number_input("Enter the Price per Week:")
B = st.number_input("Enter the Population:")
C = st.number_input("Enter the Monthly Income:")
D = st.number_input("Enter the Average Parking Per Month:")


button =st.button("Predict the no. of Weekly Riders!!")

if(button):
    model=pickle.load(open("mod.pkl","rb"))
    res = model.predict([[A,B,C,D]])[0]
    st.markdown(f"Predicted Weekly Riders are: {res}")