import os

import streamlit as st
import pandas as pd


DATAFRAME_PATH = os.getenv("DATAFRAME_PATH")
# "/Users/vinipilan/Documents/monitoramento_bancos/web-scraper/data/metrics.csv"


st.write("# Metrics")

try:
    df = pd.read_csv(DATAFRAME_PATH)
    st.write(f"The metrics were scraped in {df['date'].unique()[0]}")
    st.dataframe(df)
except:
    st.write("Some error happened in the dataframe visualization. Contact the administrator.")
