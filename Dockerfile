# ==========================================================
# Base Image
# ==========================================================

FROM python:3.10-slim


# ==========================================================
# Working Directory
# ==========================================================

WORKDIR /project


# ==========================================================
# Python Environment Settings
# ==========================================================

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Enable immediate logging output
ENV PYTHONUNBUFFERED=1


# ==========================================================
# Install Dependencies
# ==========================================================

# Copy requirements first for better Docker cache usage
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt


# ==========================================================
# Copy Application Code
# ==========================================================

COPY . .


# ==========================================================
# Application Port
# ==========================================================

EXPOSE 8000


# ==========================================================
# Start FastAPI Server
# ==========================================================

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
