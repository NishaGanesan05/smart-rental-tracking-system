from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    alert_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    asset_id = Column(
        String(20),
        ForeignKey("assets.asset_id"),
        nullable=False
    )

    alert_type = Column(
        String(50),
        nullable=False
    )

    severity = Column(
        String(20),
        nullable=False
    )

    message = Column(
        Text,
        nullable=False
    )

    detected_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    status = Column(
        String(20),
        nullable=False,
        default="OPEN"
    )

    asset = relationship("Asset", back_populates="alerts")