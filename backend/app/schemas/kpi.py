from pydantic import BaseModel


class KPIResponse(BaseModel):
    total_assets: int
    active_assets: int
    available_assets: int
    unassigned_assets: int
    active_rentals: int
    overdue_rentals: int
    returned_rentals: int
