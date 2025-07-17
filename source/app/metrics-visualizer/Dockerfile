FROM python:3.12-slim

WORKDIR /app

ADD ./main.py main.py
ADD ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 9090
ENV DATAFRAME_PATH="data/metrics.csv"

ENTRYPOINT [ "streamlit", "run", "main.py" ]
