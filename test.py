import streamlit as st


with st.sidebar.expander("Settings"):

   mode = st.selectbox("Optimization Algorithm", ["ACO", "Genetic Algorithm", "Simulated Annealing"]) 
   if mode == "ACO":
        input = st.number_input("CO₂ Emission Limit", min_value=100,max_value=1000,value=10)
        if input < 100:
           st.write("Limit is below the minimum, try again.")
