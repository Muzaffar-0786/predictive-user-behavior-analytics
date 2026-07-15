# ==========================================================
# Base Image
# ==========================================================

FROM python:3.10-slim


# ==========================================================
# Working Directory
# ==========================================================

WORKDIR /project


# ==========================================================
# Environment Variables
# ==========================================================

# Prevent Python from generating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Enable unbuffered logging
ENV PYTHONUNBUFFERED=1


# ==========================================================
# Install Dependencies
# ==========================================================

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade --no-cache-dir -r requirements.txt


# ==========================================================
# Copy Project Files
# ==========================================================

COPY . .


# ==========================================================
# Expose Application Port
# ==========================================================

EXPOSE 8000


# ==========================================================
# Start FastAPI Application
# ==========================================================

CMD [
    "uvicorn",
    "main:app",
    "--host",
    "0.0.0.0",
    "--port",
    "8000"
]
