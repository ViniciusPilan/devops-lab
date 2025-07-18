import os

import streamlit as st
import pandas as pd


DATA_PATH = os.getenv("DATA_PATH")


st.write("# Metrics")

try:
    df = pd.read_csv(f"{DATA_PATH}/metrics.csv")
    st.write(f"The metrics were scraped in {df['date'].unique()[0]}")
    st.dataframe(df)
except:
    st.write("Some error happened in the dataframe visualization. Contact the administrator.")
