#import essential libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

#load the data
df = pd.read_csv("student_data.csv", encoding='latin1')

# preprocess the data
df.columns = df.columns.str.strip().str.replace(" ","_").str.replace("-","_").str.replace(".","_")
df['College'] = df['College'].fillna('Not provided')
df['College'] = df['College'].str.strip().str.title()
df['Branch'] = df['Branch'].str.strip().str.title()
df['Course'] = df['Course'].str.strip().str.title()
df['Subject'] = df['Subject'].str.strip().str.title()

#encode features 
features = ['Branch','College','Course','Year']
target ='Subject'

df_ml =df.dropna(subset=features+[target])

encoders ={}
for col in features+[target]:
    le =LabelEncoder()
    df_ml[col]=le.fit_transform(df_ml[col])
    encoders[col]=le

#train ML model
X = df_ml[features]
y = df_ml[target]

model = RandomForestClassifier(n_estimators = 100, random_state = 42)
model.fit(X,y)

#prediction function using ML model
def predict_subject_ml(branch,college,course,year,top_n=3):
    input_df = pd.DataFrame([[branch,college,course,year]],columns=features)
    for col in features:
        input_df[col]=encoders[col].transform(input_df[col]) 
    probs = model.predict_proba(input_df)[0]
    top_indices = np.argsort(probs)[::-1][:top_n]
    subject_names = encoders[target].inverse_transform(top_indices)
    return list(zip(subject_names, probs[top_indices]))

# streamlit UI
st.title("Course Recommendation System")
st.markdown("Get top recommended course based on your College, Branch, Course, Year")

#sidebar i/p
branches = sorted(df['Branch'].dropna().unique())
colleges = sorted(df['College'].dropna().unique())
courses = sorted(df['Course'].dropna().unique())
years = sorted(df['Year'].dropna().unique())

selected_branch = st.selectbox("Select the Branch",branches)
selected_college = st.selectbox("Select the College",colleges)
selected_course = st.selectbox("Select the Course",courses)
selected_year = st.selectbox("Select the Year",years)

button = st.button("Recommended Course (ML-Based)")

if button:
    ml_recommendations = predict_subject_ml(selected_branch,selected_college,selected_course,selected_year)
    st.subheader("ML-Based Recommended Subjects")
    for i, (subject,score) in enumerate(ml_recommendations,1):
        st.markdown(f"{i}. **{subject}** -Confidence: {score:.2f}")