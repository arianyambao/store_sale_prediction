# Grab the Python base image
FROM python:3.8

# Install python and pip
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Add the scripts and resources
COPY . /app
WORKDIR /app

# Run the API inside
RUN gunicorn --bind 0.0.0.0:$PORT main:app
