from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Telemetry(Base):
    __tablename__ = "telemetry"

    telemetry_id = Column(Integer, primary_key=True, autoincrement=True)

    asset_id = Column(
        String(20),
        ForeignKey("assets.asset_id"),
        nullable=False
    )

    recorded_at = Column(
        DateTime,
        nullable=False
    )

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    engine_hours = Column(Float, nullable=True)
    runtime_hours = Column(Float, nullable=True)
    idle_hours = Column(Float, nullable=True)

    fuel_level = Column(Float, nullable=True)
    speed = Column(Float, nullable=True)

    asset = relationship("Asset", back_populates="telemetry")