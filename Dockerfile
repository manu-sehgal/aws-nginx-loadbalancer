# Start with a clean Python environment
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies inside container
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Expose application port
EXPOSE 5000

# Start Flask application
CMD ["python", "app/main.py"]