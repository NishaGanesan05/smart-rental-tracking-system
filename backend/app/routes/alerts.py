from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Alert
from app.schemas.alert import AlertResponse


router = APIRouter(prefix="/alerts", tags=["Alerts"])


@router.get("/", response_model=list[AlertResponse])
def get_alerts(db: Session = Depends(get_db)):
    return (
        db.query(Alert)
        .order_by(Alert.detected_at.desc())
        .all()
    )


@router.get("/open", response_model=list[AlertResponse])
def get_open_alerts(db: Session = Depends(get_db)):
    return (
        db.query(Alert)
        .filter(Alert.status == "OPEN")
        .order_by(Alert.detected_at.desc())
        .all()
    )


@router.get("/{asset_id}", response_model=list[AlertResponse])
def get_asset_alerts(
    asset_id: str,
    db: Session = Depends(get_db)
):
    alerts = (
        db.query(Alert)
        .filter(Alert.asset_id == asset_id)
        .order_by(Alert.detected_at.desc())
        .all()
    )

    if not alerts:
        raise HTTPException(
            status_code=404,
            detail="No alerts found for this asset"
        )

    return alerts