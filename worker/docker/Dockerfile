FROM python:3.8-slim-buster

WORKDIR /app
COPY app/ /app
COPY requirements.txt /app

RUN apt update && pip3 install -r requirements.txt

CMD ["celery", "-A", "tasks", "worker", "--loglevel", "INFO"]
