import streamlit as st

with st.sidebar.expander("Settings"):
    mode = st.selectbox("Optimization Algorithm", ["ACO", "Genetic Algorithm", "Simulated Annealing"])
    
    if mode == "ACO":
        co2_limit = st.number_input("CO₂ Emission Limit", min_value=100, max_value=1000, value=300)
        if co2_limit < 150:
            st.write("Limit is below the recommended threshold, try again.")

