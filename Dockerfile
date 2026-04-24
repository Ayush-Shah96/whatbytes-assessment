FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements/base.txt .
RUN pip install --no-cache-dir -r base.txt

# Copy project
COPY . .

# Create necessary directories
RUN mkdir -p logs media staticfiles

# Expose port
EXPOSE 8000

# Run migrations and start server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "healthcare.wsgi:application"]
