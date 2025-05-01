import streamlit as st
import dtale
from dtale.views import startup
from dtale.app import get_instance
def stDtale():

    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    if 'df' not in st.session_state or st.session_state.df is None or st.session_state.df.empty:
        st.error("Please provide the data to proceed.")
        return
    st.title("Data Editor")
 

    dataset = st.session_state.df
    if len(dataset) > 0:
        # Integrate D-Tale
        d = dtale.show(dataset, ignore_duplicate = True)
        st.write(f"D-Tale instance: {d._main_url}")
        st.components.v1.iframe(d._url, width=1100, height=800)
    else:
        st.warning("Please upload data in the Data Upload section first.")