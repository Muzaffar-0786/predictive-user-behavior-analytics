from pydantic import BaseModel, Field


# ==========================================================
# User Behavior Input Schema
# ==========================================================

class UserBehaviorCreate(BaseModel):
    """
    Schema for validating incoming user behavior data.
    """

    user_id: str = Field(
        ...,
        example="USR99281"
    )

    days_active: int = Field(
        ...,
        ge=0,
        example=12
    )

    monthly_charges: float = Field(
        ...,
        ge=0.0,
        example=59.99
    )

    support_calls: int = Field(
        ...,
        ge=0,
        example=5
    )


# ==========================================================
# User Behavior Response Schema
# ==========================================================

class UserBehaviorResponse(BaseModel):
    """
    Schema for returning stored analytics results.
    """

    id: int
    user_id: str
    days_active: int
    monthly_charges: float
    support_calls: int
    churn_risk: str
    suggested_offer: str


    class Config:
        from_attributes = True
