
# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set environment variables for Python to prevent unnecessary files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install dependencies (if there are any in requirements.txt)
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the container
COPY . .

# Define the default command to run when the container starts
CMD ["python", "main.py"]
