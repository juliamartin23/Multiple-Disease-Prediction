#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:04:52 2024

@author: juliamartin
"""

import pickle 
import streamlit as st 
from streamlit_option_menu import option_menu

# loading the saved models 

diabetes_model = pickle.load(open('/Users/juliamartin/Desktop/Coding/Multiple Disease Prediction System/Saved Models/diabetes_model.sav', 'rb'))

heart_model = pickle.load(open('/Users/juliamartin/Desktop/Coding/Multiple Disease Prediction System/Saved Models/heart_model.sav', 'rb'))

parkinsons_model = pickle.load(open('/Users/juliamartin/Desktop/Coding/Multiple Disease Prediction System/Saved Models/parkinsons_model.sav', 'rb'))
                               

# sidebar for navigation
with st.sidebar: 
    
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction', 
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity', 'heart', 'person'], 
                           
                           default_index=0)
    
# Diabetes Prediction Page 
if (selected == 'Diabetes Prediction'):
    
    # page title 
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user 
    # columns for input fields 
    col1, col2, col3 = st.columns(3)
    
    with col1: 
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2: 
        Glucose = st.text_input('Glucose Level')
        
    with col3: 
        BloodPressure = st.text_input('Blood Pressure')
        
    with col1: 
        SkinThickness = st.text_input('Skin Thickness')
        
    with col2: 
        Insulin = st.text_input('Insulin Level')
        
    with col3: 
        BMI = st.text_input('BMI')
        
    with col1: 
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
        
    with col2: 
        Age = st.text_input('Age of the Person')
    
    # code for Prediction 
    diab_diagnosis = '' 
    
    # creating a button 
    
    if st.button('Diabetes Test Result'): 
        diab_diagnosis = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if (diab_prediction[0] == 1): 
            diab_diagnosis = 'The person is diabetic'

        else: 
             diab_diagnosis = 'The person is not diabetic'     
                                      
if (selected == 'Heart Disease Prediction'):
    
    # page title 
    st.title('Heart Disease Prediction using ML')
    
    # getting the input data from the user 
    # columns for input fields 
    col1, col2, col3 = st.columns(3)
    
    with col1: 
        age = st.text_input('Age of Person')
        
    with col2: 
        sex = st.text_input('Gender')
        
    with col3: 
        cp = st.text_input('Types of Chest Pain')
        
    with col1: 
        chol = st.text_input('Serum Cholestoral in mg/dL')
        
    with col2: 
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dL')
        
    with col3: 
        restecg = st.text_input('Resting Electrocardiographic Results')
        
    with col1: 
        thalach = st.text_input('Maximum Heart Rate Achieved')
        
    with col2: 
        exang = st.text_input('Exercise Induced Angina')
        
    with col3: 
        oldpeak = st.text_input('ST Depression Induced by Exercise Relative to Reest')
        
    with col1: 
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
        
    with col2: 
        ca = st.text_input('Major Vessels Colored by Flourosopy')

    with col3: 
        thal = st.text_input('Thal: 0 = normal, 1 = fixed defect, 2 = reversible defect')
        
    with col1: 
        trestbps = st.text_input('Resting Blood Pressure')
    
    # code for Prediction 
    heart_diagnosis = ''
  
    # creating a button 
     
    if st.button('Heart Disease Test Result'): 
       heart_diagnosis = heart_model.predict([[age, sex, cp, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, trestbps]])
       
       if (heart_prediction[0] == 1): 
           heart_diagnosis = 'The person has heart disease'
       else: 
           heart_diagnosis = 'The person does not have heart disease'
        
        
    
if (selected == 'Parkinsons Disease Prediction'):
    
    # page title 
    st.title('Parkinsons Disease Prediction using ML')
    
    
    # getting the input data from the user 
    # columns for input fields 
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1: 
        fo = st.text_input('MDVP: Fo(Hz)')
        
    with col2: 
        fhi = st.text_input('MDVP: Fhi(Hz)')
        
    with col3: 
        flo = st.text_input('MDVP: FLo(Hz)')
    
    with col4: 
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
        
    with col5: 
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
    
    with col1: 
        RAP = st.text_input('MDVP: RAP')
        
    with col2: 
        PPQ = st.text_input('MDVP: PPQ')
        
    with col3: 
        DDP = st.text_input('MDVP: FLo(Hz)')
    
    with col4: 
        Shimmer = st.text_input('MDVP: Shimmer')
        
    with col5: 
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
        
    with col1: 
        APQ3 = st.text_input('Shimmer: APQ3')

    with col2: 
        APQ5 = st.text_input('Shimmer: APQ5')
        
    with col3: 
        APQ = st.text_input('Shimmer: APQ')

    with col4: 
        DDA = st.text_input('Shimmer: DDA)')
    
    with col5: 
        NHR = st.text_input('NHR')
        
    with col1: 
        HNR = st.text_input('HNR')
                            
    with col2: 
        RPDE = st.text_input('RPDE')
        
    with col3: 
        DFA = st.text_input('DFA')

    with col4: 
        spread1 = st.text_input('Spread1')
    
    with col5: 
        spread2 = st.text_input('Spread2')
        
    with col1: 
        D2 = st.text_input('D2')
                                
    with col2: 
        PPE = st.text_input('PPE')
     
    # code for Prediction 
    parkinsons_diagnosis = ''
     
    # creating a button 
     
    if st.button('Parkinsons Test Result'): 
        parkinsons_diagnosis = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
     
        if (diab_prediction[0] == 1): 
            parkinsons_diagnosis = 'The person has Parkinsons'

        else: 
            parkinsons_diagnosis = 'The person does not have Parkinsons'     
        
    
    
    
    