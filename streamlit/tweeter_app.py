import streamlit as st
import pandas as pd
import sklearn
import joblib

model = joblib.load("tweeter_classifier.joblib")
txt = st.text_input("Enter text :", "")


if (txt) :
    txt = re.sub('[^A-Za-z]+', ' ', txt.lower())
    Y_pred = model.predict_proba([txt])[0]

    if Y_pred[0] > Y_pred[1] and Y_pred[0]> Y_pred[2]:
        st.text("hate_speech")
    elif Y_pred[1] > Y_pred[0] and Y_pred[1]> Y_pred[2] :
        st.text("offensive_language")
    else :
        st.text("neither")