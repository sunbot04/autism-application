import streamlit as st
import joblib
import pandas as pd

# Load your trained SVM model
model = joblib.load('svm_model.joblib')

# Mapping for categorical variables
ethnicity_map = {
    'White-European': 0, 
    'Black': 1, 
    'Asian': 2, 
    'Hispanic': 3, 
    'Other': 4
}
contry_of_res_map = {
    'United States': 0, 'Brazil': 1, 'Spain': 2, 
                      'Egypt': 3, 'New Zealand': 4, 'Bahamas': 5, 
                      'Burundi': 6, 'Austria': 7, 'Argentina': 8, 
                      'Jordan': 9, 'Ireland': 10, 'United Arab Emirates': 11,
                      'Afghanistan': 12, 'Lebanon': 13, 'United Kingdom': 14,
                      'South Africa': 15, 'Italy': 16, 'Pakistan': 17,
                      'Bangladesh': 18, 'Chile': 19, 'France': 20, 
                      'China': 21, 'Australia': 22, 'Canada': 23, 
                      'Saudi Arabia': 24, 'Netherlands': 25, 'Romania': 26,
                      'Sweden': 27, 'Tonga': 28, 'Oman': 29, 'India': 30,
                      'Philippines': 31, 'Sri Lanka': 32, 'Sierra Leone': 33,
                      'Ethiopia': 34, 'Viet Nam': 35, 'Iran': 36,
                      'Costa Rica': 37, 'Germany': 38, 'Mexico': 39, 
                      'Russia': 40, 'Armenia': 41, 'Iceland': 42,
                      'Nicaragua': 43, 'Hong Kong': 44, 'Japan': 45,
                      'Ukraine': 46, 'Kazakhstan': 47, 'AmericanSamoa': 48,
                      'Uruguay': 49, 'Serbia': 50, 'Portugal': 51, 
                      'Malaysia': 52, 'Ecuador': 53, 'Niger': 54,
                      'Belgium': 55, 'Bolivia': 56, 'Aruba': 57, 
                      'Finland': 58, 'Turkey': 59, 'Nepal': 60, 
                      'Indonesia': 61, 'Angola': 62, 'Azerbaijan': 63,
                      'Iraq': 64, 'Czech Republic': 65, 'Cyprus': 66
}
relation_map = {
    'Self': 0, 
    'Parent': 1, 
    'Sibling': 2, 
    'Friend': 3, 
    'Other': 4
}
age_desc_map = {
    '0-3 years': 0, 
    '4-11 years': 1, 
    '12-17 years': 2, 
    '18+ years': 3
}
gender_map = {
    'f': 0,  # Female
    'm': 1   # Male
}

# Streamlit UI
st.title('Autism Screening Prediction')

# User inputs
A1_Score = st.number_input('A1 Score', min_value=0, max_value=1, value=0)
A2_Score = st.number_input('A2 Score', min_value=0, max_value=1, value=0)
A3_Score = st.number_input('A3 Score', min_value=0, max_value=1, value=0)
A4_Score = st.number_input('A4 Score', min_value=0, max_value=1, value=0)
A5_Score = st.number_input('A5 Score', min_value=0, max_value=1, value=0)
A6_Score = st.number_input('A6 Score', min_value=0, max_value=1, value=0)
A7_Score = st.number_input('A7 Score', min_value=0, max_value=1, value=0)
A8_Score = st.number_input('A8 Score', min_value=0, max_value=1, value=0)
A9_Score = st.number_input('A9 Score', min_value=0, max_value=1, value=0)
A10_Score = st.number_input('A10 Score', min_value=0, max_value=1, value=0)
age = st.number_input('Age', min_value=0, value=0)
gender = st.selectbox('Gender', options=['f', 'm'])
ethnicity = st.selectbox('Ethnicity', options=list(ethnicity_map.keys()))
jundice = st.selectbox('Jundice', options=['no', 'yes'])
contry_of_res = st.selectbox('Country of Residence', options=list(contry_of_res_map.keys()))
used_app_before = st.selectbox('Used App Before', options=['no', 'yes'])
relation = st.selectbox('Relation', options=list(relation_map.keys()))
age_desc = st.selectbox('Age Description', options=list(age_desc_map.keys()))

# Calculate result as the count of A scores with a value of 1
result = sum([
    A1_Score == 1,
    A2_Score == 1,
    A3_Score == 1,
    A4_Score == 1,
    A5_Score == 1,
    A6_Score == 1,
    A7_Score == 1,
    A8_Score == 1,
    A9_Score == 1,
    A10_Score == 1,
])

# Prepare input data
input_data = pd.DataFrame({
    'A1_Score': [A1_Score],
    'A2_Score': [A2_Score],
    'A3_Score': [A3_Score],
    'A4_Score': [A4_Score],
    'A5_Score': [A5_Score],
    'A6_Score': [A6_Score],
    'A7_Score': [A7_Score],
    'A8_Score': [A8_Score],
    'A9_Score': [A9_Score],
    'A10_Score': [A10_Score],
    'age': [age],
    'gender': [gender_map[gender]],  # Convert to numerical
    'ethnicity': [ethnicity_map[ethnicity]],  # Convert to numerical
    'jundice': [1 if jundice == 'yes' else 0],  # Convert to numerical
    'contry_of_res': [contry_of_res_map[contry_of_res]],  # Convert to numerical
    'used_app_before': [1 if used_app_before == 'yes' else 0],  # Convert to numerical
    'relation': [relation_map[relation]],  # Convert to numerical
    'age_desc': [age_desc_map[age_desc]],  # Convert to numerical
    'result': [result]  # Count of A scores with a value of 1
})

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write('Prediction:', 'Yes' if prediction[0] == 1 else 'No')
