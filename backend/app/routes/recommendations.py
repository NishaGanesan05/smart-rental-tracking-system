from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Recommendation
from app.schemas.recommendation import RecommendationResponse


router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.get("/", response_model=list[RecommendationResponse])
def get_recommendations(
    db: Session = Depends(get_db)
):
    return (
        db.query(Recommendation)
        .order_by(Recommendation.created_at.desc())
        .all()
    )


@router.get("/open", response_model=list[RecommendationResponse])
def get_open_recommendations(
    db: Session = Depends(get_db)
):
    return (
        db.query(Recommendation)
        .filter(Recommendation.status == "OPEN")
        .order_by(Recommendation.created_at.desc())
        .all()
    )


@router.get(
    "/{asset_id}",
    response_model=list[RecommendationResponse]
)
def get_asset_recommendations(
    asset_id: str,
    db: Session = Depends(get_db)
):
    recommendations = (
        db.query(Recommendation)
        .filter(Recommendation.asset_id == asset_id)
        .order_by(Recommendation.created_at.desc())
        .all()
    )

    if not recommendations:
        raise HTTPException(
            status_code=404,
            detail="No recommendations found for this asset"
        )

    return recommendations