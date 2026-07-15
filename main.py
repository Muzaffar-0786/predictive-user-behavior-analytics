from fastapi import FastAPI

from database import engine, Base
from routes import router


# ==========================================================
# Database Initialization
# ==========================================================

# Create database tables from SQLAlchemy models
Base.metadata.create_all(bind=engine)


# ==========================================================
# FastAPI Application
# ==========================================================

app = FastAPI(
    title="Predictive User Behavior Analytics MVP",
    description=(
        "A production-ready microservice built with FastAPI "
        "to analyze engagement, evaluate customer churn risks, "
        "and provide data-driven retention offers."
    ),
    version="1.0.0",
)


# ==========================================================
# Health Check Endpoint
# ==========================================================

@app.get(
    "/health",
    tags=["System Diagnostics"]
)
def health_check():
    """
    Service health monitoring endpoint.
    """

    return {
        "status": "healthy",
        "service": "user-behavior-analytics-mvp",
    }


# ==========================================================
# API Router Registration
# ==========================================================

app.include_router(router)
