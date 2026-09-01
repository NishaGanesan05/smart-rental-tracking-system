from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Rental, Asset, Customer
from app.schemas.rental import RentalCreate, RentalResponse


router = APIRouter(
    prefix="/rentals",
    tags=["Rentals"]
)


@router.get("/", response_model=list[RentalResponse])
def get_rentals(db: Session = Depends(get_db)):
    return db.query(Rental).all()


@router.get("/overdue", response_model=list[RentalResponse])
def get_overdue_rentals(db: Session = Depends(get_db)):
    return (
        db.query(Rental)
        .filter(Rental.status == "OVERDUE")
        .all()
    )


@router.get("/{rental_id}", response_model=RentalResponse)
def get_rental(
    rental_id: str,
    db: Session = Depends(get_db)
):
    rental = (
        db.query(Rental)
        .filter(Rental.rental_id == rental_id)
        .first()
    )

    if not rental:
        raise HTTPException(
            status_code=404,
            detail="Rental not found"
        )

    return rental


@router.post("/", response_model=RentalResponse)
def create_rental(
    rental_data: RentalCreate,
    db: Session = Depends(get_db)
):
    # 1. Check whether customer exists
    customer = (
        db.query(Customer)
        .filter(Customer.customer_id == rental_data.customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    # 2. Check whether asset exists
    asset = (
        db.query(Asset)
        .filter(Asset.asset_id == rental_data.asset_id)
        .first()
    )

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found"
        )

    # 3. Check whether rental ID already exists
    existing_rental = (
        db.query(Rental)
        .filter(Rental.rental_id == rental_data.rental_id)
        .first()
    )

    if existing_rental:
        raise HTTPException(
            status_code=400,
            detail="Rental ID already exists"
        )

    # 4. Check whether the asset is already actively rented
    active_rental = (
        db.query(Rental)
        .filter(
            Rental.asset_id == rental_data.asset_id,
            Rental.status.in_(["ACTIVE", "OVERDUE"])
        )
        .first()
    )

    if active_rental:
        raise HTTPException(
            status_code=400,
            detail="Asset is already rented"
        )

    # 5. Create the rental
    rental = Rental(**rental_data.model_dump())

    db.add(rental)

    # 6. Update asset status
    asset.status = "RENTED"

    db.commit()
    db.refresh(rental)

    return rental
@router.put("/{rental_id}/return", response_model=RentalResponse)
def return_rental(
    rental_id: str,
    db: Session = Depends(get_db)
):
    # 1. Find the rental
    rental = (
        db.query(Rental)
        .filter(Rental.rental_id == rental_id)
        .first()
    )

    if not rental:
        raise HTTPException(
            status_code=404,
            detail="Rental not found"
        )

    # 2. Make sure the rental is currently active
    if rental.status not in ["ACTIVE", "OVERDUE"]:
        raise HTTPException(
            status_code=400,
            detail="Rental has already been returned"
        )

    # 3. Find the associated asset
    asset = (
        db.query(Asset)
        .filter(Asset.asset_id == rental.asset_id)
        .first()
    )

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Associated asset not found"
        )

    # 4. Update rental
    from datetime import date

    rental.status = "RETURNED"
    rental.actual_return_date = date.today()

    # 5. Make asset available again
    asset.status = "AVAILABLE"

    # 6. Save both changes
    db.commit()
    db.refresh(rental)

    return rental