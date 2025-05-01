import streamlit as st
import pandas as pd

st.title("Data Profiling")
def upload_and_preview_data():
    st.title("Data Profiling")
    uploaded_file = st.file_uploader("Choose a file (CSV or Excel)", key="file_uploader", type=["csv","xlsx"])
    st.title("Data Profiling")
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
    # App title and description
    st.title("Welcome to the Automatic!")

   
    if 'startbutton' not in st.session_state:
        st.session_state.startbutton = False
    if 'df' not in st.session_state:
        st.session_state.df = None
    start_col1,start_col2 = st.columns(2)
    start_col1.markdown('<p style="color:#4FFF33; font-size: 22px; text-align: right;">To begin, click the button</p>',
                        unsafe_allow_html=True)

    start_button = start_col2.button(" Let's Start ")
    if start_button:
        st.session_state.startbutton = True

    if st.session_state.startbutton:
        file_or_not = st.radio("Do you have your own data?",["Yes","No"])
        if file_or_not == "Yes":
            st.session_state.df = upload_and_preview_data()
        elif file_or_not == "No":
            st.session_state.df = select_sample_data_page()
        if st.session_state.df is not None:
            st.write("Data Preview:")
            st.write(st.session_state.df)





