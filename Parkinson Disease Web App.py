# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 22:05:49 2022

@author: nitua
"""

import numpy as np 
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model
parkinsons_model = pickle.load(open('C:/Users/nitua/Desktop/Deploying Machine learning Model/parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Parkinsons Disease Prediction System using ML',
                          
                          ['Parkinsons Prediction'],
                          icons=['activity'],
                          default_index=0)
        
                        

# giving a title
st.title('Parkinsons Disease Web App')
    
    
# getting the input data from the user


        
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
        
       
# code for Prdiction 
       
parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person does not has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person has Parkinson's disease"
        
st.success(parkinsons_diagnosis)                                     
                                                           
                                                          
                                                           
    