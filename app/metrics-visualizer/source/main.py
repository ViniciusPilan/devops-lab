import streamlit as st
import pandas as pd


DATAFRAME_PATH = "/Users/vinipilan/Documents/monitoramento_bancos/web-scraper/data/metrics.csv"


df = pd.read_csv(DATAFRAME_PATH)

st.write("# Metrics")
st.write(f"The metrics were scraped in {df['date'].unique()[0]}")
st.dataframe(df)
