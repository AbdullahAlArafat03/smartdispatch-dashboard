import streamlit as st

with st.sidebar.expander("Tuning Panel"):
    st.number_input("Fleet Size", min_value=1,max_value=100,value=20)
