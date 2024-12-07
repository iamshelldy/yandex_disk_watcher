# Base image
FROM python:3.10-slim

# Setting work directory
WORKDIR /app

# Copying app files
COPY . .

# Installing requirements
RUN pip install --no-cache-dir -r requirements.txt

# Setting port
EXPOSE 8000

# Initializing DB
RUN flask db upgrade

# Command starting server
CMD ["gunicorn", "-b", "0.0.0.0:8000", "manage:app"]

