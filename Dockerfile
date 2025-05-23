# Use a lightweight Python base image
FROM python:3.9-slim

# Set environment variables - keeps Python from writing .pyc files and buffers stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
# This step is only re-run if requirements.txt changes
COPY requirements.txt ./

# Install dependencies
# Use --no-cache-dir to avoid storing cache in the image
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
# This step is re-run if any of your code files change
COPY . .

# Run the application
CMD ["python", "entrypoint.py"]
