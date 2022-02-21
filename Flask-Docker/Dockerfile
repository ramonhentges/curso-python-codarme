FROM python:3.10.1

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP app.py
ENV FLASK_ENV development

RUN useradd -m python

WORKDIR /home/python/app

RUN mkdir app

ADD ./requirements.txt /home/python/app

# Install any needed packages specified in requirements.txt as root
RUN pip install -r requirements.txt
RUN pip install autopep8

# Change to local user
USER python
