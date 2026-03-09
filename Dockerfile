# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project code including frontend
COPY . .

# Expose the port Cloud Run expects
EXPOSE 8080

# Run Uvicorn and use the PORT env variable from Cloud Run
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080} --workers 1"]