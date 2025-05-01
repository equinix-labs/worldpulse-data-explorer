import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_option_menu import option_menu
from streamlit_pandas_profiling import st_profile_report


def stProfile():
    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    if 'df' not in st.session_state or st.session_state.df is None or st.session_state.df.empty:
        st.error("Please provide the data to proceed.")
        return

    st.info("Please note that there may be a processing delay during data profiling.")

    dataset = st.session_state.df
    df_profile = dataset.copy()
    object_cols = df_profile.select_dtypes(include=['object']).columns
    df_profile[object_cols] = df_profile[object_cols].astype('category')
    viz_tab_op = option_menu(
        menu_title="Profiling Reports",
        options=["Minimal Mode", "Medium Mode", "Maximal Mode"],
        orientation='horizontal',
    )
    if viz_tab_op == "Minimal Mode":
        profile_report = ProfileReport(df_profile, minimal=True,dark_mode=True)
        st_profile_report(profile_report)
    elif viz_tab_op == "Medium Mode":
        profile_report = ProfileReport(df_profile,explorative=True, correlations = None, interactions = None,dark_mode=True)
        st_profile_report(profile_report)
    elif viz_tab_op == "Maximal Mode":
        profile_report = ProfileReport(df_profile,dark_mode=True)
        export = profile_report.to_html()
        st.download_button(label="Download Full Report", data=export, file_name='report.html')
        st_profile_report(profile_report)