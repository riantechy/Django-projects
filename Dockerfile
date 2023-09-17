# Use an official Python runtime as the base image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql-dev \
    && apk add --no-cache postgresql-libs

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project code
COPY . .

# Create the media directory inside the container (optional)
RUN mkdir -p /app/media

# Collect static files
RUN python manage.py collectstatic --no-input --traceback

# Define the volume or host mount for media files
VOLUME /etc/django/media:/app/media

# Expose the port on which the Django development server will run
EXPOSE 8000

# Run migrations and start the Django development server
CMD python manage.py makemigrations && \
    # python manage.py migrate --fake sessions zero &&\
    # python manage.py migrate --fake admin zero &&\
    # python manage.py migrate --run-syncdb && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000









