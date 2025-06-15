# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy backend code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (adjust depending on FastAPI/Flask)
EXPOSE 8000

# Start backend server (example for FastAPI)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
