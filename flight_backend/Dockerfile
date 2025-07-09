# Use the official Python 3.10 image as the base image
FROM python:3.10

# Prevent Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

# Force the stdout and stderr streams to be unbuffered (useful for Docker logs)
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy the dependencies list to the working directory
COPY requirements.txt ./

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project directory contents into the container
COPY . .

# Expose port 8000 (default Django development server port)
EXPOSE 8000

# Command to run the Django development server on container startup
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
