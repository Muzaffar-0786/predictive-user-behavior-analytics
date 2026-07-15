from sqlalchemy import Column, Integer, Float, String

from database import Base


# ==========================================================
# User Behavior Analytics Model
# ==========================================================

class UserBehavior(Base):
    """
    SQLAlchemy ORM model for storing user behavior
    analytics and churn prediction results.
    """

    __tablename__ = "user_behavior_analytics"


    # Primary Identifier
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    # User Information
    user_id = Column(
        String,
        index=True,
        nullable=False
    )


    # User Activity Metrics
    days_active = Column(
        Integer,
        nullable=False
    )

    monthly_charges = Column(
        Float,
        nullable=False
    )

    support_calls = Column(
        Integer,
        nullable=False
    )


    # Analytics Output
    churn_risk = Column(
        String,
        nullable=False
    )

    suggested_offer = Column(
        String,
        nullable=False
    )
