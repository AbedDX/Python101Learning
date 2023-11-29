# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the server script into the container
COPY Server.py /app

# Expose port 15000
EXPOSE 15000

# Run the server script
CMD ["python", "Server.py"]