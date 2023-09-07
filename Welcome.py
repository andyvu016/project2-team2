import streamlit as st

st.set_page_config(
    page_title="Welcome and Disclaimer"
)

st.write("# Welcome")

st.sidebar.success("Select a Health Condition to Predict Above")

st.markdown(
    """
    ### "CHECK FIRST"
    "Check First" is an app created specifically to analyze health-related risk behaviors, chronic health conditions, 
    and the use of preventive services connected to the risk for COPD(Chronic Obstructive Pulmonary Disease) and Dementia.

    The focus of this project is to use Machine Learning and Deep Learning models to determine the risk of common health diseases.

    More details can be found on the project's GitHub repository [here](https://github.com/andyvu016/project2-team2)

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
