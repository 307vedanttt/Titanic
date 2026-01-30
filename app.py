import streamlit as st
import pickle
import numpy as np

with open("titanic_model.pkl", "rb") as f:
    model = pickle.load(f)


st.title("Titanic Survival Prediction")

pclass=st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex=st.selectbox("Gender", ["Male", "Female"])
age=st.number_input("Age",2,80,15)
sibsp=st.number_input("Number of Siblings/Spouses Aboard",0,10,0)
parch=st.number_input("Number of Parents/Children Aboard",0,3,0)
fare=st.number_input("Ticket Fare",0.0,600.0,30.0)
embarked=st.selectbox("Port of Embarkation", ["Cherbourg", "Queenstown", "Southampton"])

sex_num = 1 if sex == "Male" else 0
embarked_mapping = {"Cherbourg": 0, "Queenstown": 1, "Southampton": 2}
embarked_num = embarked_mapping[embarked]

input_data = np.array([[pclass, sex_num, age, sibsp, parch, fare, embarked_num]]) 

if st.button("Predict Survival"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("The passenger is predicted to have survived.")
    else:
        st.error("The passenger is predicted to have not survived.")