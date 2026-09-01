from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Asset, Rental
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

    return {
        "total_assets": total_assets,
        "active_assets": active_assets,
        "available_assets": available_assets,
        "unassigned_assets": unassigned_assets,
        "active_rentals": active_rentals,
        "overdue_rentals": overdue_rentals,
        "returned_rentals": returned_rentals,
    }
