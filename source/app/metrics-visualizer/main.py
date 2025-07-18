import os

import streamlit as st
import pandas as pd


st.write("# Metrics")

try:
    df = pd.read_csv("metrics.csv")
    st.write(f"The metrics were scraped in {df['date'].unique()[0]}")
    st.dataframe(df)
except:
    st.write("Some error happened in the dataframe visualization. Contact the administrator.")
