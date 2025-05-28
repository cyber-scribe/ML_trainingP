import streamlit as st
import pickle
st.title(" Score prediction App")

sh = st.number_input("Enter the number of Study hours:")

button =st.button("Predict the Score!!")

if(button):
    model=pickle.load(open("res.pkl","rb"))
    res = model.predict([[sh]])[0]
    if(sh> 10):
        st.markdown(f"Invalid input")
    else:
        st.markdown(f"Predicted Score is : {res}")