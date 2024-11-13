!pip install joblib
!pip install pandas numpy scikit-learn

import streamlit as st
import joblib
import pandas as pd

# Load your trained SVM model
model = joblib.load('svm_model.joblib')

# Mapping for categorical variables
ethnicity_map = {
    'White-European': 0, 'Black': 1, 'Asian': 2, 'Hispanic': 3, 'Other': 4
}
country_of_res_map = {
    'United States': 0, 'Brazil': 1, 'Spain': 2, 'Egypt': 3, 'New Zealand': 4,
    'Bahamas': 5, 'Burundi': 6, 'Austria': 7, 'Argentina': 8, 'Jordan': 9,
    'Ireland': 10, 'United Arab Emirates': 11, 'Afghanistan': 12, 'Lebanon': 13,
    'United Kingdom': 14, 'South Africa': 15, 'Italy': 16, 'Pakistan': 17,
    'Bangladesh': 18, 'Chile': 19, 'France': 20, 'China': 21, 'Australia': 22,
    'Canada': 23, 'Saudi Arabia': 24, 'Netherlands': 25, 'Romania': 26,
    'Sweden': 27, 'Tonga': 28, 'Oman': 29, 'India': 30, 'Germany': 31
}

st.title("Autism Screening Application")

# Input fields
st.subheader("Please fill out the following information:")
ethnicity = st.selectbox("Ethnicity", list(ethnicity_map.keys()))
country_of_residence = st.selectbox("Country of Residence", list(country_of_res_map.keys()))
age = st.slider("Age", 0, 100, 25)
jaundice = st.selectbox("Have you been diagnosed with jaundice?", ["Yes", "No"])
family_history = st.selectbox("Family history of autism?", ["Yes", "No"])
screening_score = st.slider("Screening Score", 0, 20, 10)

# Preprocess inputs for the model
ethnicity_val = ethnicity_map[ethnicity]
country_of_res_val = country_of_res_map[country_of_residence]
jaundice_val = 1 if jaundice == "Yes" else 0
family_history_val = 1 if family_history == "Yes" else 0

# Create a DataFrame to match the model input
# Adjust input_data to have 19 features by adding placeholder columns (assuming missing values should be zero)
input_data = pd.DataFrame([[ethnicity_val, country_of_res_val, age, jaundice_val, family_history_val, screening_score] + [0]*13],
                          columns=['ethnicity', 'country_of_res', 'age', 'jaundice', 'family_history', 'screening_score'] + ['feature_'+str(i) for i in range(7, 20)])


# Predict and display result
if st.button("Predict Autism Screening"):
    prediction = model.predict(input_data)
    result = "Positive for Autism Risk" if prediction[0] == 1 else "Negative for Autism Risk"
    st.subheader("Screening Result:")
    st.write(result)
