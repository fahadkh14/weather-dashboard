# ===========================
# Base Image
# ===========================
FROM python:3.12-slim

# ===========================
# Environment Variables
# ===========================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ===========================
# Working Directory
# ===========================
WORKDIR /app

# ===========================
# Install Dependencies
# ===========================
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ===========================
# Copy Project Files
# ===========================
COPY . .

# ===========================
# Expose Flask Port
# ===========================
EXPOSE 5000

# ===========================
# Start Flask Application
# ===========================
CMD ["python", "app.py"]
