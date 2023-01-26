import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.write("App by Theophilus Onyejiaku")
selection = st.sidebar.selectbox("Explore or Make Prediction", ("Make a Prediction", "Explore about COVID19 Cases"))
picklefile = open("logistic_model.pki", "rb")
model = pickle.load(picklefile)


usmer = [1, 2]
#medical_unit = range(1, 13)
sex = [1, 2]
patient_type = [1, 2]
pneumonia = [1, 2]
age = range(5, 110)
diabetes = [1, 2]
copd = [1, 2]
asthma = [1, 2]
inmsupr = [1, 2]
hypertension = [1, 2]
other_disease  = [1, 2]
cardiovascular = [1, 2]
obesity = [1, 2]
renal_chronic = [1, 2]
tobacco = [1, 2]
#classification_final = range(1, 7)
icu = [1,2]

if selection == "Make a Prediction":
    st.title("""Diagnostically Predict if a Patient is Likely to Survive COVID-19""")
    st.write("""Stand in place of the patient while answering the following questions""")
    usmer = st.selectbox("Did you treat medical units of the first, second or third level ('Yes' =1, 'No' = 2)", usmer)
    medical_units = st.number_input("Input the level of institution of the Natinal Health System that provided the care", min_value=1, max_value=13)
    sex = st.selectbox("Are you male or female? ('Female'=1, 'Male'=2)", sex)
    patient_type = st.selectbox("Type of care you received in the unit (1-'returned home', 2-'hospitalization')", patient_type)
    pneumonia = st.selectbox("Do you have air sacs inflamation? (1-'yes', 2-'no')", pneumonia)
    age = st.number_input("How old are you?", min_value=1, max_value=110)
    diabetes = st.selectbox("Are you diabetic? (1-'yes', 2-'no')", diabetes)
    copd = st.selectbox("Do you have chronic obstructive pulmonary disease? (1-'yes', 2-'no')", copd)
    asthma =  st.selectbox("Are you asthmatic? (1-'yes', 2-'no')", asthma)
    inmsupr = st.selectbox("Are you immunosuppressed? (1-'yes', 2-'no')", inmsupr)
    hypertension =st.selectbox("Are you hypertensive? (1-'yes', 2-'no')", hypertension)
    other_disease = st.selectbox("Do you suffer from other disease? (1-'yes', 2-'no')", other_disease)
    cardiovascular = st.selectbox("Do you have heart or blood vessel related diseases? (1-'yes', 2-'no')", cardiovascular)
    obesity = st.selectbox("Are you obesse? (1-'yes', 2-'no')", obesity)
    renal_chronic = st.selectbox("Do you have chronic renal disease or not?", renal_chronic)
    tobacco = st.selectbox("Do you use tobacco or not? (1-'yes', 2-'no')", tobacco)
    classification_final = st.number_input("What is your covid test findings? Choose between 1-7", min_value=1, max_value=7)

    my_column = [usmer, medical_units, sex, patient_type, pneumonia, age,
                 diabetes, copd, asthma, inmsupr, hypertension, other_disease,
                 cardiovascular, obesity, renal_chronic, tobacco, classification_final]
    a = np.array([my_column])
    prediction = st.button("Make Prediction")
    if prediction:
        answers = model.predict(a)
        if answers == 1:
            st.write("Thanks Goodness, Patient is likely to survive :smiley:")
        else:
            st.write("Sorry, Patient is likely to Die :pensive:")


if selection == "Explore about COVID19 Cases":
    st.title("Exploratory Page")
    option = st.selectbox("Kindly Pick one of the options from the drop down", ["Top Countries with Most Active Cases",
                                                                                "Top Countries with Most Deaths Cases",
                                                                                "Top Countries of Recovered Cases"])
    countrywise_df = pd.read_csv('country_wise_latest.csv')
    activeCaseinCountries = countrywise_df[['Country/Region', 'Active']].sort_values(by=['Active'], ascending=False).head(10)
    DeathCaseinCountries = countrywise_df[['Country/Region','Deaths']].sort_values(by=['Deaths'],ascending=False).head(10)
    RecoveredCaseinCountries = countrywise_df[['Country/Region', 'Recovered']].sort_values(by=['Recovered'], ascending=False).head(10)

    if option == "Top Countries with Most Active Cases":
        fig = px.bar(activeCaseinCountries, x='Active', y='Country/Region', color='Country/Region', title='Top 10 Countries of Most Active Cases')
        st.plotly_chart(fig, use_container_width=True)

    elif option == "Top Countries with Most Deaths Cases":
        fig = px.bar(DeathCaseinCountries, x='Deaths', y='Country/Region', color='Country/Region', title='Top 10 Countries of Deaths Cases')
        st.plotly_chart(fig, use_container_width=True)
    elif option == "Top Countries of Recovered Cases":
        fig = px.bar(RecoveredCaseinCountries, x='Recovered', y='Country/Region', color='Country/Region', title='Top 10 Countries of Recovered Cases')
        st.plotly_chart(fig, use_container_width=True)