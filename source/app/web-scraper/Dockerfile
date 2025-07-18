# docker build -t web-scraper:1.0.0 . --no-cache

FROM python:3.12-slim

WORKDIR /app

ADD ./main.py main.py
ADD ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "python", "main.py" ]
