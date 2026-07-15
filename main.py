from fastapi import FastAPI, status

from app.database import Base, engine
from app.routes import router as analytics_router


# ==========================================================
# Database Initialization
# ==========================================================

# Create all database tables automatically during application startup
Base.metadata.create_all(bind=engine)


# ==========================================================
# FastAPI Application
# ==========================================================

app = FastAPI(
    title="Predictive User Behavior Analytics MVP",
    version="1.0.0",
    description=(
        "Production-ready FastAPI service to predict user churn "
        "and automate targeted retention rewards."
    ),
)


# ==========================================================
# Register API Routers
# ==========================================================

app.include_router(analytics_router)


# ==========================================================
# Root Endpoint
# ==========================================================

@app.get(
    "/",
    tags=["Root"],
    status_code=status.HTTP_200_OK
)
def read_root():
    """
    Root endpoint that provides basic information
    about the API service.
    """

    return {
        "project": "Predictive User Behavior Analytics MVP",
        "status": "healthy",
        "documentation_url": "/docs",
    }


# ==========================================================
# Health Check Endpoint
# ==========================================================

@app.get(
    "/health",
    tags=["Root"],
    status_code=status.HTTP_200_OK
)
def health_check():
    """
    Health check endpoint used by deployment
    platforms to verify service availability.
    """

    return {
        "status": "ok",
        "service": "active",
    }
