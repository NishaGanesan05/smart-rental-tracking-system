from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TelemetryResponse(BaseModel):
    telemetry_id: int
    asset_id: str
    recorded_at: datetime
    latitude: float | None = None
    longitude: float | None = None
    engine_hours: float | None = None
    runtime_hours: float | None = None
    idle_hours: float | None = None
    fuel_level: float | None = None
    speed: float | None = None

    model_config = ConfigDict(from_attributes=True)


class TelemetrySummary(BaseModel):
    asset_id: str
    average_runtime_hours: float
    average_idle_hours: float
    average_fuel_level: float
    utilization_percentage: float