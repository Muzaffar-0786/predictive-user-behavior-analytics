from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.database import get_db
from app.models import UserBehavior
from app.schemas import UserBehaviorCreate, UserBehaviorResponse


# ==========================================================
# Router Configuration
# ==========================================================

router = APIRouter(
    prefix="/analytics",
    tags=["User Behavior Analytics"]
)


# ==========================================================
# Business Logic
# ==========================================================

def calculate_churn_risk(days_active: int, support_calls: int) -> tuple[str, str]:
    """
    Calculate user churn risk and determine the best retention offer.
    """

    if days_active < 30 or support_calls > 4:
        return (
            "HIGH",
            "50% Discount Coupon + 1 Month Free Premium"
        )

    if support_calls > 2:
        return (
            "MEDIUM",
            "Feature Guide Email + 10% Loyalty Bonus"
        )

    return (
        "LOW",
        "Regular Feature Update Newsletter"
    )


# ==========================================================
# Analyze User Behavior
# ==========================================================

@router.post(
    "/analyze",
    response_model=UserBehaviorResponse,
    status_code=status.HTTP_201_CREATED
)
def analyze_user_behavior(
    payload: UserBehaviorCreate,
    db: Session = Depends(get_db)
):
    """
    Analyze user behavior, calculate churn risk,
    save the result to the database,
    and return the stored record.
    """

    # Calculate prediction
    churn_risk, suggested_offer = calculate_churn_risk(
        payload.days_active,
        payload.support_calls
    )

    # Create database object
    db_user = UserBehavior(
        user_id=payload.user_id,
        days_active=payload.days_active,
        monthly_charges=payload.monthly_charges,
        support_calls=payload.support_calls,
        churn_risk=churn_risk,
        suggested_offer=suggested_offer,
    )

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    except SQLAlchemyError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database transaction failed."
        )


# ==========================================================
# Get Analytics Logs
# ==========================================================

@router.get(
    "/logs",
    response_model=list[UserBehaviorResponse],
    status_code=status.HTTP_200_OK
)
def get_analytics_logs(
    db: Session = Depends(get_db)
):
    """
    Retrieve all user behavior analytics records.
    Latest records are returned first.
    """

    try:
        logs = (
            db.query(UserBehavior)
            .order_by(UserBehavior.id.desc())
            .all()
        )

        return logs

    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch analytics logs."
        )
