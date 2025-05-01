import pandas as pd
import streamlit as st
from classification_pycaret import classificationPycaret
from regression_pycaret import regressionPycaret


@st.cache_data
def data_load():
    if 'df' in st.session_state:
        return st.session_state.df
        
def ml_models():

    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    if 'df' not in st.session_state or st.session_state.df is None or st.session_state.df.empty:
        st.error("Please provide the data to proceed.")
        return
    st.title("AutoML Using Pycaret")
    st.markdown("""
    Automate your machine learning workflow with [PyCaret](https://pycaret.org)
    """)
    st.info("Please note that there may be some processing delay during the AutoML execution.")

    dataset = data_load()


    if len(dataset) > 0:
        # Using HTML to apply the custom style to the selectbox label
        type_ml = st.selectbox('Select ML model', ["Regression", "Classification", "Clustering", "Anomaly detection",
                                                   "Time series"])

        st.write(f"You selected: {type_ml}")
        if type_ml == "Classification":
            classificationPycaret()
        elif type_ml == "Regression":
            regressionPycaret()
   
    else:
        st.error("Please provide the data to proceed.")