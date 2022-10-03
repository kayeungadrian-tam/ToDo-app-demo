FROM python:3.9-slim-buster

WORKDIR /app/
COPY ./backend/requirements.txt .

RUN pip install -U pip \
    &&  pip install --no-cache-dir -r requirements.txt

expose 8000