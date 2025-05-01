import streamlit as st
import pandas as pd
from st_aggrid import AgGrid  # Assuming you're using AgGrid for displaying the DataFrame

def upload_and_preview_data():
    # Your data upload logic here
    # For example, using file uploader
    uploaded_file = st.file_uploader("Upload your data file", type=["csv", "xlsx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            return pd.read_excel(uploaded_file)
    return None

def dataupload_page():
    # Initialize session state variables
    if 'df' not in st.session_state:
        st.session_state.df = None

    # Upload and preview data
    st.session_state.df = upload_and_preview_data()
    
    if st.session_state.df is not None:
        # Display the uploaded data using AgGrid
        dataset = st.session_state.df
        AgGrid(dataset)

        # Get the number of rows and columns
        num_rows, num_cols = dataset.shape
        
        # Display success message with number of rows and columns
        st.success(f"Data has been successfully loaded! The dataset contains {num_rows} rows and {num_cols} columns.")


        

