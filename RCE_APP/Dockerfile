FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy app files to have the code in the container
COPY code/app_rce.py /app/

# Install Flask because we use it on our application
RUN pip install Flask

# Expose port to connect to it
EXPOSE 5000

# Run the app to enable it on the container
CMD ["python", "app_rce.py"]

