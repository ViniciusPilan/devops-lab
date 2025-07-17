import os

from minio import Minio
import streamlit as st
import pandas as pd


BUCKET_HOST = os.getenv("BUCKET_HOST")
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")


# Create client with access key and secret key with specific region.
client = Minio(
    BUCKET_HOST,
    access_key=ACCESS_KEY_ID,
    secret_key=SECRET_ACCESS_KEY,
    secure=False
)

client.fget_object("app", "metrics.csv", "metrics.csv")

st.write("# Metrics")

try:
    df = pd.read_csv("metrics.csv")
    st.write(f"The metrics were scraped in {df['date'].unique()[0]}")
    st.dataframe(df)
except:
    st.write("Some error happened in the dataframe visualization. Contact the administrator.")
