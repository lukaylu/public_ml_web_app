#importing the dependencies
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

heart_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinson_model = pickle.load(open('parkinson_model2.sav','rb'))


#creating the sidebar navigation menu
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Prediction'],
                           icons= ['activity','heart','person'],
                           
                           default_index=0)

#page title
if (selected=='Diabetes Prediction'):
    st.title('Diabetes Predictions Using ML') 
    
    #getting the user's input data
    #columns for input fields
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    diab_diagnosis = ''
    
    #creating the button
    if st.button('Diabetes Test Result'):
        diab_predictions = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_predictions[0]==1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is not Diabetic'
    st.success(diab_diagnosis)
            
#page title
if (selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction Using ML')
    
    #getting the user's input data
    #columns for input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of the Person')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain Type')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')     
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electro Cardiographic Results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('exercise induced angina')
    with col1:
        oldpeak = st.text_input('oldpeak')
    with col2:
        slope = st.text_input('the slope: of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels: colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    heart_diagnosis = ''
    
    #creating button
    if st.button('Heart Disease Result'):
        
        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The Patient has Heart Disease'
        else:
            heart_diagnosis = 'The Patient does not have Heart Disease'
    st.success(heart_diagnosis)
            
#page title
if (selected=='Parkinson Prediction'):
    st.title('Parkinsons Prediction Using ML')
    
    #getting the user's input data
    #columns for input fields
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        fo = st.text_input("MDVP_Fo(Hz)")

    with col2:
        fhi = st.text_input('MDVP_Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP_Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP_Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP_Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP_RAP')

    with col2:
        PPQ = st.text_input('MDVP_PPQ')

    with col3:
        DDP = st.text_input('Jitter_DDP')

    with col4:
        Shimmer = st.text_input('MDVP_Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP_Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer_APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer_APQ5')

    with col3:
        APQ = st.text_input('MDVP_APQ')

    with col4:
        DDA = st.text_input('Shimmer_DDA')

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
        
    park_diagnosis = ''
    
    #creating button
    if st.button('Parkinson Disease Result'):
        
        park_prediction = parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if (park_prediction[0]==1):
            park_diagnosis = 'The Patient has Parkinson Disease'
        else:
            park_diagnosis = 'The Patient does not have Parkinson Disease'
    st.success(park_diagnosis)

