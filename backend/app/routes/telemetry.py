from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Asset, Telemetry
from app.schemas.telemetry import TelemetryResponse, TelemetrySummary


router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"]
)


@router.get("/", response_model=list[TelemetryResponse])
def get_telemetry(db: Session = Depends(get_db)):
    return (
        db.query(Telemetry)
        .order_by(Telemetry.recorded_at.desc())
        .all()
    )


@router.get("/{asset_id}", response_model=list[TelemetryResponse])
def get_asset_telemetry(
    asset_id: str,
    db: Session = Depends(get_db)
):
    asset = (
        db.query(Asset)
        .filter(Asset.asset_id == asset_id)
        .first()
    )

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found"
        )

    return (
        db.query(Telemetry)
        .filter(Telemetry.asset_id == asset_id)
        .order_by(Telemetry.recorded_at.desc())
        .all()
    )


@router.get("/{asset_id}/summary", response_model=TelemetrySummary)
def get_telemetry_summary(
    asset_id: str,
    db: Session = Depends(get_db)
):
    asset = (
        db.query(Asset)
        .filter(Asset.asset_id == asset_id)
        .first()
    )

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found"
        )

    result = (
        db.query(
            func.avg(Telemetry.runtime_hours),
            func.avg(Telemetry.idle_hours),
            func.avg(Telemetry.fuel_level)
        )
        .filter(Telemetry.asset_id == asset_id)
        .first()
    )

    if not result or result[0] is None:
        raise HTTPException(
            status_code=404,
            detail="No telemetry data found for asset"
        )

    average_runtime = float(result[0] or 0)
    average_idle = float(result[1] or 0)
    average_fuel = float(result[2] or 0)

    total_operating_time = average_runtime + average_idle

    if total_operating_time > 0:
        utilization = (
            average_runtime / total_operating_time
        ) * 100
    else:
        utilization = 0

    return {
        "asset_id": asset_id,
        "average_runtime_hours": round(average_runtime, 2),
        "average_idle_hours": round(average_idle, 2),
        "average_fuel_level": round(average_fuel, 2),
        "utilization_percentage": round(utilization, 2)
    }