# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10.1

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN useradd -m python

WORKDIR /home/python/app

RUN mkdir app

ADD ./requirements /home/python/app/requirements

# Install any needed packages specified in requirements.txt as root
RUN pip install -r ./requirements/dev.txt

# Change to local user
USER python