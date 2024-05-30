# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:40:37 2024

@author: KesBes
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:02:37 2024

@author: KesBes
"""
# Load the libraries needed for deployment

import numpy as np
import streamlit as st
import pickle
from streamlit_option_menu import option_menu
    
# Load the models

Decision_Tree_Model = pickle.load(open('C:/Users/Fatima/Desktop/HealthCare/dt.sav', 'rb'))

Random_Forest_Model = pickle.load(open('C:/Users/Fatima/Desktop/HealthCare/rf.sav', 'rb'))

Support_Vector_Machine_Model = pickle.load(open('C:/Users/Fatima/Desktop/HealthCare/svm.sav', 'rb'))

# Create a sidebar menu for nagivation

with st.sidebar:
    selection = option_menu('Diabetes Prediction System', 
                            ['DT Prediction',
                               'RF Prediction',
                               'SVM Prediction'],
                            icons=['tree','tree-fill', 'activity'],
                            default_index = 0)

# Selection Option 
# Decision Tree Selection

if selection == 'Decison Tree Prediction':
# Give the page for Decision tree option
    st.title('Using ML- Decision Tree Algorithm')
    col1, col2 = st.columns(2)
    
        # Inputs for the first column
        							
    
        
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies:', key='Pregnancies')
        Glucose = st.text_input('Glucose Level:', key='Glucose')
        BloodPressure = st.text_input('Blood Pressure Reading:', key='BloodPressure')
        SkinThickness = st.text_input('Skin Thickness:', key='SkinThickness')
        Insulin = st.text_input('Insulin Level:', key='Insulin')

    # Inputs for the second column
    with col2:
        # cibil_score = st.text_input('Cibil Score:', key='cibil_score')
        BMI = st.text_input('Body  Mass Index Value:', key='BMI')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function:', key='DiabetesPedigreeFunction')
        Age = st.text_input('Page Age:', key='Age')
    
elif selection == 'Random Forest Prediction':
# Give the page for Random Forest option
    st.title('Using ML - Random Forest Algorithm')

else:
# Give the page for Decision tree option
    st.title('Using ML - Support Vector Algorithm')