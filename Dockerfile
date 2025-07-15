# Base image with Python 3.10 slim version
FROM python:3.10-slim

# Prevent Python from writing .pyc files and enable unbuffered output (logs immediately)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install system dependencies required for mysqlclient and netcat
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential pkg-config netcat-openbsd

# Copy requirements and wait-for-it script to container
COPY requirements.txt /app/
COPY wait-for-it.sh /app/wait-for-it.sh

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make wait-for-it.sh executable (for waiting MySQL availability)
RUN chmod +x /app/wait-for-it.sh

# Copy application source code into container
COPY . /app/

# Expose port 5000 for Flask app
EXPOSE 5000

# Default command to run Flask app (if not overridden by compose)
CMD ["python", "run.py"]
