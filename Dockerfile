# Use an official Python runtime as a parent image
FROM python:3.11.4

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files into the container
COPY . /app/

# Command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
