# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 00:22:04 2025

@author: DELL
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
heart_model = pickle.load(open('HeartDisease Model.sav', 'rb'))
breastcancer_model = pickle.load(open('breastcancer_model.sav', 'rb'))
diabetes_model = pickle.load(open('diabetes_trained_model.sav', 'rb'))

# creating a sidebar
with st.sidebar:
    
    selection = option_menu('Multiple Disease Prediction System',
                            
                            ['Diabetes Prediction',
                             'Heart Disease Prediction',
                             'Breast Cancer Prediction',
                             'Parkinsons Disease Prediction'],
                             
                            icons=['lungs','heart','bandaid-fill','file-medical-fill'],
                            
                            default_index = 0)
    
    
# Diabetes prediction page

if(selection == 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction System')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Pregnancies Number')
    
    with col2:
        Glucose = st.text_input('Level of Glucose')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure status')
    
    with col1:
        SkinThickness = st.text_input('Thickness of Skin')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI Value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function level')
    
    with col2:
        Age = st.text_input('Age of a Person')
    
    
    # Prediction
    diab_diagnosis = ''
    
    # creating a button
    
    if st.button('Diabetes Test Result'):
        diabetes_pred = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
        if(diabetes_pred[0]==0):
            diab_diagnosis = 'The Person is not diabetic'
            
        else:
            diab_diagnosis = 'The person has Diabetes'
            
    st.success(diab_diagnosis)

    
    
# Heart Disease prediction page

    
if(selection == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction System')
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex: 0 = female: 1=male')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        


    # creating a button
    heart_diagnosis = ''
    
    # Convert all inputs to numeric
    try:
        age = int(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = int(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = int(ca)
        thal = int(thal)
    except ValueError:
            st.error("Please enter only numeric values.")



    
    if st.button('Heart Disease Test Result'):
        heart_pred = heart_model.predict([[int(age), int(sex), int(cp), float(trestbps), float(chol),
                                   int(fbs), int(restecg), int(thalach), int(exang),
                                   float(oldpeak), int(slope), int(ca), int(thal)]])
    
    
        if(heart_pred[0]==0):
            heart_diagnosis = 'The person does not have a heart disease'
            
        else:
            heart_diagnosis = 'The person has Heart disease'
            
    st.success(heart_diagnosis)

            
            

# Breast cancer prediction page

    
if(selection == 'Breast Cancer Prediction'):
    
    st.title('Breast Cancer Prediction System')

    col1, col2, col3, col4, col5 = st.columns(5)
    
    
    with col1:
        mean_radius = st.text_input('Mean Radius')
    
    with col2:
        mean_texture = st.text_input('Mean Texture')
    
    with col3:
        mean_perimeter = st.text_input('Mean Perimeter')
    
    with col4:
        mean_area = st.text_input('Mean Area')
    
    with col5:
        mean_smoothness = st.text_input('Mean Smoothness')
    
    with col1:
        mean_compactness = st.text_input('Mean Compactness')
    
    with col2:
        mean_concavity = st.text_input('Mean Concavity')
    
    with col3:
        mean_concave_points = st.text_input('Mean Concave Points')
    
    with col4:
        mean_symmetry = st.text_input('Mean Symmetry')
    
    with col5:
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')
    
    with col1:
        radius_error = st.text_input('Radius Error')
    
    with col2:
        texture_error = st.text_input('Texture Error')
    
    with col3:
        perimeter_error = st.text_input('Perimeter Error')
    
    with col4:
        area_error = st.text_input('Area Error')
    
    with col5:
        smoothness_error = st.text_input('Smoothness Error')
    
    with col1:
        compactness_error = st.text_input('Compactness Error')
    
    with col2:
        concavity_error = st.text_input('Concavity Error')
    
    with col3:
        concave_points_error = st.text_input('Concave Points Error')
    
    with col4:
        symmetry_error = st.text_input('Symmetry Error')
    
    with col5:
        fractal_dimension_error = st.text_input('Fractal Dimension Error')
    
    
    with col1:
        worst_radius = st.text_input('Worst Radius')
    
    with col2:
        worst_texture = st.text_input('Worst Texture')
    
    with col3:
        worst_perimeter = st.text_input('Worst Perimeter')
    
    with col4:
        worst_area = st.text_input('Worst Area')
    
    with col5:
        worst_smoothness = st.text_input('Worst Smoothness')
    
    with col1:
        worst_compactness = st.text_input('Worst Compactness')
    
    with col2:
        worst_concavity = st.text_input('Worst Concavity')
    
    with col3:
        worst_concave_points = st.text_input('Worst Concave Points')
    
    with col4:
        worst_symmetry = st.text_input('Worst Symmetry')
    
    with col5:
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')
    
    # creating a button
    brst_diagnosis = ''
    
    if st.button('Breast Cancer Test Result'):
        brst_pred = breastcancer_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]])
    
        if(brst_pred[0]==0):
            brst_diagnosis = 'It is a Malignant Breast Cancer'
        
        else:
            brst_diagnosis = 'It is a Benign Breast Cancer'
        
    st.success(brst_diagnosis)
    

if(selection == 'Parkinsons Disease Prediction'):
    
    st.title('Parkinsons Disease Prediction System')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')

    
    
    # Parkinsons Prediction Page
    park_diagnosis = ''
    
    # creating a button
    
    if st.button('Parkinsons Disease Test Result'):
            input_data = (float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                      float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                      float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR),
                      float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE))


            parkinsons_pred = parkinsons_model.predict([input_data])

            if parkinsons_pred[0] == 0:
                park_diagnosis = 'The Person is healthy and does not have a disease'
            else:
                park_diagnosis = 'The person has a Parkinsons disease'
      

    st.success(park_diagnosis)
    
    

        


            
    

    
    
    
