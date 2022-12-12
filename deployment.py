import numpy as np
import pandas as pd
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('model.sav', 'rb'))

# creating a function for Prediction
def prediction(age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wbcc,rbcc,htn,dm,cad,appet,pe,ane):

    if rbc == 'Normal':
        rbc = 1
    elif rbc == 'Abnormal':
        rbc = 0

    if pc == 'Normal':
        pc = 1
    elif pc == 'Abnormal':
        pc = 0

    if pcc == 'Present':
        pcc = 1
    elif pcc == 'Not Present':
        pcc = 0

    if ba == 'Present':
        ba = 1
    elif ba == 'Not Present':
        ba = 0

    if htn == 'Yes':
        htn = 1
    elif htn == 'No':
        htn = 0

    if dm == 'Yes':
        dm = 1
    elif dm == 'No':
        dm = 0

    if cad == 'Yes':
        cad = 1
    elif cad == 'No':
        cad = 0

    if appet == 'Yes':
        appet = 1
    elif appet == 'No':
        appet = 0

    if pe == 'Yes':
        pe = 1
    elif pe == 'No':
        pe = 0

    if ane == 'Yes':
        ane = 1
    elif ane == 'No':
        ane = 0

    prediction = loaded_model.predict(pd.DataFrame([[age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wbcc,rbcc,htn,dm,cad,appet,pe,ane]],
                columns=['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv','wbcc','rbcc','htn','dm','cad','appet','pe','ane']))
    print(prediction)

    if (prediction[0] == 0):
        return ('The person does not have Chronic Kidney Disease')
    else:
        return ('The person has Chronic Kidney Disease')


def main():

    # giving a title
    st.title('CKD Prediction Web App')
    st.image("https://img.freepik.com/free-vector/hand-drawn-urology-illustration_23-2149707560.jpg?w=2000")

    # getting the input data from the user
    age = st.number_input('Age:', min_value=1.0, max_value=130.0, value=1.0)
    bp = st.number_input('Blood Pressure:', min_value=0.0, max_value=200.0, value=1.0)
    sg = st.number_input('Specific Gravity:', min_value=1.0, max_value=10, value=1.0)
    al = st.number_input('Albumin:', min_value=0.0, max_value=100.0, value=1.0)
    su = st.number_input('Sugar:', min_value=0.0, max_value=100.0, value=1.0)
    rbc = st.selectbox('Red Blood Cells', ['Normal', 'Abnormal'])
    pc = st.selectbox('Pus Cell', ['Normal', 'Abnormal'])
    pcc = st.selectbox('Pus Cell Clumps', ['Present', 'Not Present'])
    ba = st.selectbox('Bacteria', ['Present', 'Not Present'])
    bgr = st.number_input('Blood Glucose Random:', min_value=0.0, value=1.0)
    bu = st.number_input('Blood Urea:', min_value=0.0, value=1.0)
    sc = st.number_input('Serum Creatinine:', min_value=0.0, value=1.0)
    sod = st.number_input('Sodium:', min_value=0.0, value=1.0)
    pot = st.number_input('Potassium:', min_value=0.0, value=1.0)
    hemo = st.number_input('Hemoglobin:', min_value=0.0, value=1.0)
    pcv = st.number_input('Packed  Cell Volume:', min_value=0.0, value=1.0)
    wbcc = st.number_input('White Blood Cell Count:', min_value=0.0, value=1.0)
    rbcc = st.number_input('Red Blood Cell Count:', min_value=0.0, value=1.0)
    htn = st.selectbox('Hypertension', ['Yes', 'No'])
    dm = st.selectbox('Diabetes Mellitus', ['Yes', 'No'])
    cad = st.selectbox('Coronary Artery Disease', ['Yes', 'No'])
    appet = st.selectbox('Appetite', ['Yes', 'No'])
    pe = st.selectbox('Pedal Edema', ['Yes', 'No'])
    ane = st.selectbox('Anemia', ['Yes', 'No'])

    diagnosis = ''
    # creating a button for Prediction
    if st.button('CKD Test Result'):
        diagnosis = prediction(age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wbcc,rbcc,htn,dm,cad,appet,pe,ane)

    st.success(diagnosis)


if __name__ == '__main__':
    main()
