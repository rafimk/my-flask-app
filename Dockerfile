# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container

# Define environment variable
ENV NAME World

ENV API_PORT=80

# Expose the API port
EXPOSE $API_PORT

# Run app.py when the container launches
CMD ["python", "app.py"]
