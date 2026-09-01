from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    recommendation_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    asset_id = Column(
        String(20),
        ForeignKey("assets.asset_id"),
        nullable=False
    )

    recommendation_type = Column(
        String(50),
        nullable=False
    )

    priority = Column(
        String(20),
        nullable=False
    )

    message = Column(
        Text,
        nullable=False
    )

    reason = Column(
        Text,
        nullable=False
    )

    status = Column(
        String(20),
        nullable=False,
        default="OPEN"
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    asset = relationship(
        "Asset",
        back_populates="recommendations"
    )