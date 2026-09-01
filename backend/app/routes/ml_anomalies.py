from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.ml_anomaly import MLAnomalyResponse
from app.services.ml_anomaly_detection import detect_ml_anomalies


router = APIRouter(
    prefix="/ml",
    tags=["ML Anomaly Detection"]
)


@router.get(
    "/anomalies",
    response_model=list[MLAnomalyResponse]
)
def get_ml_anomalies(
    db: Session = Depends(get_db)
):
    return detect_ml_anomalies(db)


@router.get(
    "/anomalies/{asset_id}",
    response_model=list[MLAnomalyResponse]
)
def get_asset_ml_anomalies(
    asset_id: str,
    db: Session = Depends(get_db)
):
    results = detect_ml_anomalies(db)

    return [
        result
        for result in results
        if result["asset_id"] == asset_id
    ]