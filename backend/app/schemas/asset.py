from pydantic import BaseModel, ConfigDict


class AssetResponse(BaseModel):
    asset_id: str
    asset_type: str
    model: str | None = None
    serial_number: str | None = None
    status: str
    site_id: str | None = None

    model_config = ConfigDict(from_attributes=True)