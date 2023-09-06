import ast
import streamlit as st
from prediction import predict_dementia, predict_copd

st.title("Predicting Chronic Obstructive Pulmonary Disease (C.O.P.D.) Risk")

st.markdown("Machine learning model to predict C.O.P.D. Risk based on various health factors.")

st.header("Please answer the following about you.")

age = st.number_input("Age(Years):", min_value = 0.0, max_value = 120.0)

sex = st.selectbox("Sex:", ["Male", "Female"])

height = st.number_input("Height(Meters):", min_value = 0.0, max_value = 3.0)

weight = st.number_input("Weight(Kilograms):", min_value = 0.0, max_value = 500.0)

genhlth = st.selectbox("How would you say in general your health is?", 
                       ["Don't Know/Not Sure", "Excellent", "Very Good", "Good", "Fair", "Poor"])

exercise = st.selectbox("During the past month, other than your regular job, \
                        did you participate in any physical activities or exercises such as running, \
                        calisthenics, golf, gardening, or walking for exercise?", ["Don't Know/Not Sure", "No", "Yes"])

asthma = st.selectbox("Have you had or been told you had asthma?", ["Don't Know/Not Sure", "No", "Yes"])

cancer = st.selectbox("Have you had or been told you had cancer?", ["Don't Know/Not Sure", "No", "Yes"])

diabetes = st.selectbox("Have you had or been told you had diabetes?", ["No", "No, but pre-diabetes or borderline diabetes", "Yes", "Yes, but female and only during pregnancy"])

pneuvac = st.selectbox("Have you ever had a pneumonia shot also known as a pneumococcal vaccine?", ["Don't Know/Not Sure", "No", "Yes"])

smoker = st.selectbox("What is your smoker status?", ["Never smoked", "Former smoker", "Someday smoker", "Everyday smoker"])

ecig = st.selectbox("What is your E-cigarette/Vaping status?", ["Not currently using E-cigarettes", "Current E-cigarette user"])

fruit = st.number_input("In the last 30 days, what is the total number of fruits you consumed?", min_value = 0.0, max_value = 9999.0)

veges = st.number_input("In the last 30 days, what is the total number of vegetables you consumed?", min_value = 0.0, max_value = 9999.0)

potato = st.number_input("On average, how many servings of potatoes, or sweet potatoes, such as baked, boiled, mashed potatoes, or potato salad do you consume per day?", min_value = 0.0, max_value = 9999.0)

fries = st.number_input("In the last 30 days, how many times had you consumed french fries?", min_value = 0.0, max_value = 9999.0)

if st.button("Predict C.O.P.D. Risk"):
    data = {
        "age": age,
        "sex": sex,
        "height": height,
        "weight": weight,
        "genhlth": genhlth,
        "exercise": exercise,
        "asthma": asthma,
        "cancer": cancer,
        "diabetes": diabetes,
        "pneuvac": pneuvac,
        "smoker": smoker,
        "ecig": ecig,
        "fruit": (fruit/30),
        "veges": (veges/30),
        "potato": potato,
        "fries": (fries/30)
    }

    with st.spinner('Please wait while the predition is being made...'):
        prediction = predict_copd(data)

    if prediction == 0:
        st.success(f"You are not at risk of C.O.P.D.!")
        st.markdown("This was result was determined by a Gaussian Naive Bayes Machine Learning Model with an accuracy of 85%")
    else:
        st.success(f"You are at risk of C.O.P.D.!")
        st.markdown("This was result was determined by a Gaussian Naive Bayes Machine Learning Model with an accuracy of 85%")