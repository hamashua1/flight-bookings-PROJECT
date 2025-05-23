# Use a lightweight Python base image
FROM Python 3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

# for testing purpose1
# Install dependencies (if any)
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "entrypoint.py"]
