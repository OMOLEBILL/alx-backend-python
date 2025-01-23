# Use official Python 3.10 image
FROM python:3.10

# Set environment variables to prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a working directory
WORKDIR /app

# Copy requirements.txt before the rest of your code for efficient caching
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose port 8000 to enable external access to the app
EXPOSE 8000

# Start Django on port 8000 when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
