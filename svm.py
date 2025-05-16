import streamlit as st
import pickle
st.title(" Purchasing prediction App")

Age = st.number_input("Enter the Age:")
sal = st.number_input("Enter the Salary:")

button =st.button("Predict!!")

if(button):
    model=pickle.load(open("svm.pkl","rb"))
    res = model.predict([[Age,sal]])[0]
    if(res):
        R='Yes'
    else:
        R='No'
    st.markdown(f"Predicted purchasing is : {R}")