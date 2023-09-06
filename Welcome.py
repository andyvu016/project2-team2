import streamlit as st

st.set_page_config(
    page_title="Welcome and Disclaimer"
)

st.write("# Welcome")

st.sidebar.success("Select a Health Condition to Predict Above")

st.markdown(
    """
    ### Introduction
    *Insert intro here*

    ### Collaborators
    Emily Blackstein </br>
    Harshita Panchal </br>
    Andy Vu </br>
    Amar Sen

    ### Resources
    - [2021 BRFSS Survey Data and Documentation](https://www.cdc.gov/brfss/annual_data/annual_2021.html)
    - [NHAMCS Datasets and Documentation](https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm)

    ### Medical Disclaimer !! For any symptoms seek professional help. This information is purely for educational purpose.
"""
)
