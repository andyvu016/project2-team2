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
    **Emily Blackstein** \n
    **Harshita Panchal** \n
    **Andy Vu** \n
    **Amar Sen**

    ### Resources
    - [2021 BRFSS Survey Data and Documentation](https://www.cdc.gov/brfss/annual_data/annual_2021.html)
    - [NHAMCS Datasets and Documentation](https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm)

    ### Disclaimer
    For educational purposes...this is not medical diagnosis...seek profesional help.
"""
)