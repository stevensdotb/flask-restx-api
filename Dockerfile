# Use an official Python runtime as an image
FROM python:3.8

EXPOSE 5000

WORKDIR /airports

ENV FLASK_APP=run.py
ENV FLASK_CONFIG=development

COPY . /airports
RUN pip install --no-cache-dir -r requirements.txt