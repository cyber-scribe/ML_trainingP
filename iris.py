import streamlit as st
import pickle
st.title(" Iris Classifier App")

sl = st.number_input("Enter the Sepal Length:")
sw = st.number_input("Enter the Sepal Width:")
pl = st.number_input("Enter the Petal Length:")
pw = st.number_input("Enter the Petal Width:")

button =st.button("Predict the Iris Class !!")

if(button):
    model=pickle.load(open("iris.pkl","rb"))
    res = model.predict([[sl,sw,pl,pw]])[0]
    st.markdown(f"Predicted Iris Class is : {res}")