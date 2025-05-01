import streamlit as st
from streamlit_option_menu import option_menu
from pygwalker.api.streamlit import StreamlitRenderer
#from auto_viz import autoVizs

def pywalkr(dataset):
    try:
        pyg_app = StreamlitRenderer(dataset)
        pyg_app.explorer()
    except Exception as e:
        st.error(str(e))
def visualizatn():

    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    if 'df' not in st.session_state or st.session_state.df is None or st.session_state.df.empty:
        st.error("Please provide the data to proceed.")
        return
    #st.title("Visualization")
  

    dataset = st.session_state.df
    viz_tab_op = option_menu(
        menu_title="Visualization",
        options=["Custom Visualization", "Auto Visualization"],
        orientation='horizontal',
    )
    if viz_tab_op == "Auto Visualization":
         pywalkr(dataset)
    elif viz_tab_op == "Custom Visualization":
        pywalkr(dataset)

