import streamlit as st
import pandas as pd

def resource_page():
    st.title("Automated Data Profiling and Visualization Tool Overview")
    st.divider()
    # Change the color of the main text
    st.markdown("""
    <div style="color: #e39844;">
        This tool is an interactive, web-based application built with Streamlit that automates data profiling, exploratory data analysis (EDA), and visualization for structured datasets.
It integrates leading open-source libraries such as pandas-profiling (now ydata-profiling), D-Tale, and PyWalker to streamline the data understanding process for data analysts, data scientists, and business users.

    """, unsafe_allow_html=True)

    st.markdown("""
    
        ## Goals:
        - Automate the process of understanding the structure, quality, and insights of tabular datasets.
        - Provide a low-code, user-friendly interface for data profiling and visualization.
        - Enable rapid iteration and early data quality checks during data science or reporting projects. 
        - Combine multiple EDA tools in a single, unified platform for convenience and extensibility.
        
       
    
    """, unsafe_allow_html = True)
      # Change the color of the emphasized text
    st.markdown("""
    
        ## Core Features:   
    
    """, unsafe_allow_html = True)
    
    st.markdown("""
    <div style="color: green;">

                
📁 Data Upload Interface
                
•	Supports .csv, .xlsx, and .json file formats.
                
•	Configuration options for:
                
o	Delimiter
                
o	Encoding
                
o	Sheet selection (for Excel)
                
                
📑 Automated Profiling with Pandas Profiling
                
•	One-click generation of full EDA reports.
                
•	Includes:
                
o	Summary statistics
                
o	Correlation heatmaps
                
o	Missing value analysis
                
o	Duplicate checks
                
o	Variable distributions
                
                
📊 Interactive Exploration with D-Tale
                
•	Spreadsheet-like UI for data frame interaction.
                
•	Features include:
                
o	Sorting & filtering
                
o	Data type editing
                
o	Summary stats
                
o	Inline visualizations
                
                
📈 Auto EDA with PyWalker
                
•	Automatic generation of:
                
o	Distribution plots
                
o	Correlation visuals
                
o	Categorical comparisons
                
•	Minimal user configuration required.
                
                
🧾 Metadata Overview
                
•	Displays:
                
o	Row & column count
                
o	Data types
                
o	Memory usage
                
o	Null value counts
                
o	Unique values per column
                
 
🧱 Architecture & Tech Stack
                
Component	Technology Used
                
Web App Framework	Streamlit
                
Data Profiling	pandas-profiling / ydata-profiling
                
Data Exploration	D-Tale
                
Auto Visualizations	PyWalker
                
Data Handling	pandas
                
UI/UX Layer	Streamlit widgets
                
 
📦 Key Python Packages
                
Package	Purpose
                
pandas	Core data manipulation
                
ydata-profiling	Automated data profiling
                
dtale	Spreadsheet-like data exploration
                
pywalker	Automatic EDA visualizations
                
streamlit	Web application frontend


    """, unsafe_allow_html=True)
