import streamlit as st
from streamlit_option_menu import option_menu
from home import home_page
from DataUpload import dataupload_page
from Data_Dtale import stDtale
from Data_Profile_WP import stProfile
from visualization import visualizatn
from categorical import resource_page


 # Page setup
st.set_page_config(
    page_title="World Pulse Data Explorer",
    page_icon="📊",
    layout="wide",
)


def main():
    # Initialize session state variables if they don't exist
    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    if 'df' not in st.session_state:
        st.session_state.df = None

    # Sidebar content
    with st.sidebar:
        # Other sidebar elements
        st.sidebar.image("logo_image.png", width=500,use_column_width=True)
        # Option menu in sidebar
        pages = ["Home", "Data Upload", "Manipulation", "Profiling", "Visualization",  "About", "Contact"]
        nav_tab_op = option_menu(
            menu_title="Menu",
            options=pages,
            icons=['house', 'chat', 'pencil-square' ,'file-earmark-bar-graph', 'bar-chart-line', 'info-circle', 'envelope'],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "5!important","background-color":"#C0C0C0"},
                "icon": {"color": "#333333", "font-size": "25px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "color":"#333333","--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#e69138"},
            }
        )

       
    # Main content of the app
    if nav_tab_op == "Home":
        home_page()
    elif nav_tab_op == "Data Upload":
        dataupload_page()
    elif nav_tab_op == "Manipulation":
        stDtale()
    elif nav_tab_op == "Profiling":
        stProfile()
    elif nav_tab_op == "Visualization":
        visualizatn()
    elif nav_tab_op == "Resources":
        resource_page()   
 
if __name__ == "__main__":
    main()
