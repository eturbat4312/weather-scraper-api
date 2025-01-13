# Use official Python image
FROM python:3.11

# Create a working directory inside the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Default command to run the scraper when the container starts
CMD ["python", "api.py"]
