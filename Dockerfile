FROM python:3.9.3-slim
LABEL maintainer="Development team <mohamed.elzomor@outlook.com>"

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
