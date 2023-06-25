FROM python:3.11.0-slim-buster

WORKDIR /TAESC_Backend

RUN apt update && \
    apt upgrade -y && \
    apt install -y \
    openssl \
    gettext \
    postgresql \
    postgresql-contrib

WORKDIR /TAESC_Backend

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /TAESC_Backend .

EXPOSE 8000
