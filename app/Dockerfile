# Grab the Python base image
FROM python:3.8

# Install python and pip
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Add our code
COPY . /app
WORKDIR /app

# Run the API inside
RUN gunicorn main:app -b :$PORT
