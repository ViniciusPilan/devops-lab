# docker build -t metrics-visualizer:1.0.0 . --no-cache

FROM python:3.12-slim

WORKDIR /app

ADD ./main.py main.py
ADD ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "streamlit", "run", "main.py", "--server.port", "8080", "--server.address", "0.0.0.0" ]
