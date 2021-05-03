import streamlit as st
import numpy as np
import pickle

def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


model = load_model()

regressor = model["model"]
le_country = model["le_country"]
le_education = model["le_education"]


def show_predict_page():
    st.title('Software Developer Salary Prediction')
    st.write("### We need some information to predict:")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Country", sorted(countries))
    education = st.selectbox("Education Level", education)

    experience = st.slider("Years of Experience", 0, 50, 3)

    button_clicked = st.button("Calculate Salary")
    if button_clicked:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

