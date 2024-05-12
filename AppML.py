import streamlit as st
import pickle
import urllib.request

# Function to load pickled files from URL
def load_pickled_files(url):
    with urllib.request.urlopen(url) as f:
        return pickle.load(f)

# Load the pickled files from GitHub URLs
feature_dict_url = 'https://github.com/Qasim-Kazmi/Qasim-Kazmi/raw/main/my_feature_dict.pkl'
pipeline_url = 'https://github.com/Qasim-Kazmi/Qasim-Kazmi/raw/main/pipeline.pkl'

feature_dict = load_pickled_files(feature_dict_url)
pipeline = load_pickled_files(pipeline_url)

# Function to preprocess input features
def preprocess_input(input_features):
    # You might need to preprocess the input features here if required
    return input_features

# Function to make predictions
def predict(input_features):
    preprocessed_features = preprocess_input(input_features)
    prediction = pipeline.predict(preprocessed_features)
    return prediction

# Streamlit UI
st.title('Prediction App')

# User input form
st.write('Enter the values for prediction:')
user_input = {}
for feature, value in feature_dict.items():
    user_input[feature] = st.number_input(feature, value=value)

# Predictions
if st.button('Predict'):
    prediction = predict([list(user_input.values())])
    st.write('Prediction:', prediction[0])
