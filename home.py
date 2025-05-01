import streamlit as st
import pandas as pd
#from st_aggrid import GridOptionsBuilder, AgGrid,

def upload_and_preview_data():
    uploaded_file = st.file_uploader("Choose a file (CSV or Excel)", key="file_uploader", type=["csv","xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                try:
                    df = pd.read_csv(uploaded_file)
                except Exception as e:
                    st.error(str(e))
            elif uploaded_file.name.endswith(('.xlsx', '.xls')):
                try:
                    df = pd.read_excel(uploaded_file)
                except Exception as e:
                    st.error(str(e))
            # st.write("Data Preview:")
            # st.write(df)
            return df
        except Exception as e:
            st.error(f"Error reading file: {e}")
    return st.session_state.df





def home_page():
    st.title("Welcome to World Pulse Data Explorer")
    st.divider()
    # Change the color of the main text
    st.markdown("""
    <div style="color: #e39844;">
        This application allows you to explore, prepare your data, and extract insights in record time. Our platform empowers users of all levels to understand their data better and make data-driven decisions with. We offer a user-friendly interface, powerful visualizations, and advanced tools to help you truly unleash the potential of your data.
    </div>
    """, unsafe_allow_html=True)

    # Change the color of the emphasized text
    st.markdown("""
    <div style="color: green;">
        *** No coding or prior machine learning knowledge required.***
    </div>
    """, unsafe_allow_html=True)
    
    # the color of the key features section
    st.markdown("""
    
        ## Key Features:
        - Easy data upload and profiling
        - Natural language querying for data exploration/manipulation/visualization
        - Interactive Tableau-Like visualizations 
        - Machine Learning model prototyping
        
        Get started by uploading your data in the 'Data Upload' section!
    
    """, unsafe_allow_html = True)

