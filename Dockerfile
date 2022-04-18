# Pull the base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get upgrade -y

RUN apt-get update -y

RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y

WORKDIR /app

#Upgrade pip
RUN pip install pip -U
ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD . /usr/src/app