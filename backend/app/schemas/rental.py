from datetime import date

from pydantic import BaseModel, ConfigDict


class RentalBase(BaseModel):
    customer_id: str
    asset_id: str
    start_date: date
    expected_return_date: date
    actual_return_date: date | None = None
    status: str = "ACTIVE"


class RentalCreate(RentalBase):
    rental_id: str


class RentalResponse(RentalBase):
    rental_id: str

    model_config = ConfigDict(from_attributes=True)