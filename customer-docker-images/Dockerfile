# Base Image
FROM python:3.12-slim

# Metadata
LABEL maintainer="Pranay Shukla"

# Set Working Directory
WORKDIR /app

# Copy requirements file
COPY app/requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY app/ .

# Environment Variable
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "main.py"]
