from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AlertResponse(BaseModel):
    alert_id: int
    asset_id: str
    alert_type: str
    severity: str
    message: str
    detected_at: datetime
    status: str

    model_config = ConfigDict(from_attributes=True)