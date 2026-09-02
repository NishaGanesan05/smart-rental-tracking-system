from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Asset, Rental, Telemetry, Alert
from app.schemas.kpi import KPIResponse


router = APIRouter(
    prefix="/kpis",
    tags=["KPIs"]
)


@router.get("/", response_model=KPIResponse)
def get_kpis(db: Session = Depends(get_db)):

    total_assets = db.query(Asset).count()

    active_assets = (
        db.query(Asset)
        .filter(Asset.status == "ACTIVE")
        .count()
    )

    available_assets = (
        db.query(Asset)
        .filter(Asset.status == "AVAILABLE")
        .count()
    )

    unassigned_assets = (
        db.query(Asset)
        .filter(Asset.status == "UNASSIGNED")
        .count()
    )

    active_rentals = (
        db.query(Rental)
        .filter(Rental.status == "ACTIVE")
        .count()
    )

    overdue_rentals = (
        db.query(Rental)
        .filter(Rental.status == "OVERDUE")
        .count()
    )

    returned_rentals = (
        db.query(Rental)
        .filter(Rental.status == "RETURNED")
        .count()
    )
    telemetry_records = db.query(Telemetry).all()

    if telemetry_records:
        total_runtime = sum(
            record.runtime_hours or 0
            for record in telemetry_records
        )

        total_idle = sum(
            record.idle_hours or 0
            for record in telemetry_records
        )

        total_operating_time = total_runtime + total_idle

        if total_operating_time > 0:
            fleet_utilization = (
                total_runtime / total_operating_time
            ) * 100
        else:
            fleet_utilization = 0.0
    else:
        fleet_utilization = 0.0

    active_alerts = (
        db.query(Alert)
        .filter(Alert.status == "OPEN")
        .count()
    )

    return {
        "total_assets": total_assets,
        "active_assets": active_assets,
        "available_assets": available_assets,
        "unassigned_assets": unassigned_assets,
        "active_rentals": active_rentals,
        "overdue_rentals": overdue_rentals,
        "returned_rentals": returned_rentals,
        "fleet_utilization": round(fleet_utilization, 2),
        "active_alerts": active_alerts
        }
