import streamlit as st


with st.sidebar.expander("Settings"):

  mode == st.radio(""Choose Settings Mode", ["Basic", "Advanced"])

  if mode == "Basic":
    st.selectbox("Basic", ["Basic 1", "Basic 2", "Basic 3"])
  elif mode == "Advanced":
    st.selectbox("Advanced", ["Advanced 1", "Advanced 2", "Advanced 3"])
