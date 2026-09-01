from pydantic import BaseModel


class MLAnomalyResponse(BaseModel):
    telemetry_id: int
    asset_id: str
    is_anomaly: bool
    anomaly_score: float
    anomaly_status: str
    runtime_hours: float | None = None
    idle_hours: float | None = None
    fuel_level: float | None = None
    speed: float | None = None