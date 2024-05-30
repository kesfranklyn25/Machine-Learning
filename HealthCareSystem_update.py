# Load required libraries

# import numpy as np
import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Load models

dt = pickle.load(open('dt.sav','rb'))
rf = pickle.load(open('rf.sav','rb'))
svm = pickle.load(open('svm.sav','rb'))

# Create a sidebar menu for the models
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #ff000050;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    selection = option_menu('Menu', 
                            ['DT Prediction',
                            'RF Prediction',
                            'SVM Prediction'],
                            icons = ['tree', 'tree-fill', 'activity'],
                            default_index = 0)

if selection == 'DT Prediction':
    # Give the page a title
    st.title('ML- Prediction Using Decision Tree')
    col1, col2 = st.columns(2)
    # Get user data for prediction
    with col1:
        
        Pregnancies = st.text_input('No of Pregnacies', placeholder = 'Enter an interger value', key ='Pregnancies')
        Glucose = st.text_input('Glucose Level', placeholder = 'Enter glucose level', key = 'Glucose')
        BloodPressure = st.text_input('Blood Pressure Level', placeholder = 'Enter blood pressure reading', key = 'BloodPressure')
        SkinThickness = st.text_input('SkinThickness', placeholder = 'Skin Thickness', key = 'SkinThickness')
    with col2:
        

        Insulin = st.text_input('Insulin',placeholder = 'Enter Insulin Level', key = 'Insulin')
        BMI = st.text_input('Body Mass Index',placeholder = 'BMI value', key = 'BMI')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function',placeholder = 'DPF', key = 'DiabetesPedigreeFunction')
        Age = st.text_input('Patient Age',placeholder = "Patient\'s age", key = 'Age')

    prediction = ''
    with col1:
        if st.button('Diabetes Test Result'):
            outcome = dt.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,
                          Insulin,BMI,DiabetesPedigreeFunction,
                          Age]])
            if outcome[0] == 1:
                prediction = 'DIABETIC'
            else:
                prediction = 'NOT DIABETIC'
            
    with col2:
        st.success(prediction)

elif selection == 'RF Prediction':
    # Give the page a title
    st.title('ML- Prediction Using Random Forest')
    col1, col2 = st.columns(2)
    # Get user data for prediction
    with col1:
        
        Pregnancies = st.text_input('No of Pregnacies', placeholder = 'Enter an interger value', key ='Pregnancies')
        Glucose = st.text_input('Glucose Level', placeholder = 'Enter glucose level', key = 'Glucose')
        BloodPressure = st.text_input('Blood Pressure Level', placeholder = 'Enter blood pressure reading', key = 'BloodPressure')
        SkinThickness = st.text_input('SkinThickness', placeholder = 'Skin Thickness', key = 'SkinThickness')
    with col2:
        

        Insulin = st.text_input('Insulin',placeholder = 'Enter Insulin Level', key = 'Insulin')
        BMI = st.text_input('Body Mass Index',placeholder = 'BMI value', key = 'BMI')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function',placeholder = 'DPF', key = 'DiabetesPedigreeFunction')
        Age = st.text_input('Patient Age',placeholder = "Patient\'s age", key = 'Age')

    prediction = ''
    with col1:
        if st.button('Diabetes Test Result'):
            outcome = rf.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,
                          Insulin,BMI,DiabetesPedigreeFunction,
                          Age]])
            if outcome[0] == 1:
                prediction = 'DIABETIC'
            else:
                prediction = 'NOT DIABETIC'
            
    with col2:
        st.success(prediction)

else:
    # Give the page a title
    st.title('ML- Prediction Using Support Vector Machine')
    col1, col2 = st.columns(2)
    # Get user data for prediction
    with col1:
        
        Pregnancies = st.text_input('No of Pregnacies', placeholder = 'Enter an interger value', key ='Pregnancies')
        Glucose = st.text_input('Glucose Level', placeholder = 'Enter glucose level', key = 'Glucose')
        BloodPressure = st.text_input('Blood Pressure Level', placeholder = 'Enter blood pressure reading', key = 'BloodPressure')
        SkinThickness = st.text_input('SkinThickness', placeholder = 'Skin Thickness', key = 'SkinThickness')
    with col2:
        

        Insulin = st.text_input('Insulin',placeholder = 'Enter Insulin Level', key = 'Insulin')
        BMI = st.text_input('Body Mass Index',placeholder = 'BMI value', key = 'BMI')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function',placeholder = 'DPF', key = 'DiabetesPedigreeFunction')
        Age = st.text_input('Patient Age',placeholder = "Patient\'s age", key = 'Age')

    prediction = ''
    with col1:
        if st.button('Diabetes Test Result'):
            outcome = svm.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,
                          Insulin,BMI,DiabetesPedigreeFunction,
                          Age]])
            if outcome[0] == 1:
                prediction = 'DIABETIC'
            else:
                prediction = 'NOT DIABETIC'
            
    with col2:
        st.success(prediction)
