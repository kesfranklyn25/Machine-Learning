# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Web interface

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Fatima/Desktop/Projects/Loan_Approval_Prediction/Loan_Approval_Model.sav', 'rb'))

# user_input = (3, 1, 0, 9100000, 29700000, 20, 506, 7100000, 4500000, 33300000, 12800000) # loan application for approval
# Function to predict loan approval or rejection using our predictive model
def loan_prediction(user_data):
    user_input_np_array = np.asarray(user_data) # convert the input to a numpy array
    user_input_reshape = user_input_np_array.reshape(1, -1) # reshape the input_numpy_array
    prediction = loaded_model.predict(user_input_reshape)
#     print(prediction)
    if prediction[0] == 0:
        return 'Loan rejected'
    else:
        return 'The Customer is likely to repay the loan; you can approve '

# lona_prediction function ends here

# main function starts here
import streamlit as st

def main():
    # st.title("Loan Prediction App")
    
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Loan Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Define the layout using the columns feature
    col1, col2 = st.columns(2)

    # Inputs for the first column
    with col1:
        no_of_dependents = st.text_input('Number of Dependents:', key='no_of_dependents')
        education = st.text_input('Graduate (1) or Non-graduate (0):', key='education')
        self_employed = st.text_input('Self Employed (1) or Not (0):', key='self_employed')
        income_annum = st.text_input('Annual Income:', key='income_annum')
        loan_amount = st.text_input('Loan Amount Requested:', key='loan_amount')
        loan_term = st.text_input('Proposed Loan Tenor:', key='loan_term')

    # Inputs for the second column
    with col2:
        cibil_score = st.text_input('Cibil Score:', key='cibil_score')
        residential_assets_value = st.text_input('Residential Asset Value:', key='residential_assets_value')
        commercial_assets_value = st.text_input('Commercial Asset Value:', key='commercial_assets_value')
        luxury_assets_value = st.text_input('Luxury Asset Value:', key='luxury_assets_value')
        bank_asset_value = st.text_input('Bank Asset Value:', key='bank_asset_value')

        approval = ''
        if st.button('Predict'):
            approval = loan_prediction([no_of_dependents, education, self_employed, income_annum, loan_amount,
                                      loan_term, cibil_score, residential_assets_value, commercial_assets_value, 
                                      luxury_assets_value, bank_asset_value])
            st.success(approval)

if __name__ == "__main__":
    main()
