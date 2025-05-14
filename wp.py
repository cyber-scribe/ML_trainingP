import streamlit as st
import pickle
st.title("Weather Prediction App")

pn = st.number_input("Enter Precipitation:")
maxt = st.number_input("Enter the Maximum Temperature:")
mint = st.number_input("Enter the Minimum Temperature:")
wins = st.number_input("Enter the Wind Speed:")

button =st.button("Predict the Weather!!")

if(button):
    lr=pickle.load(open("wp.pkl","rb"))
    res = lr.predict([[pn,maxt,mint,wins]])[0]
    st.markdown(f"Today's weather conditions: {res}")