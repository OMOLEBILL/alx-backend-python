FROM python:3.10

# Set environment variables to prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a working directory
WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r /app/messaging_app/requirements.txt

EXPOSE 8000

# Start Django on port 8000 when the container starts -p 8000:8000
CMD ["python3", "/app/manage.py", "runserver", "0.0.0.0:8000"]
