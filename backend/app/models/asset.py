from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database import Base


class Asset(Base):
    __tablename__ = "assets"

    asset_id = Column(String(20), primary_key=True)
    asset_type = Column(String(50), nullable=False)
    model = Column(String(50), nullable=True)
    serial_number = Column(String(100), nullable=True)
    status = Column(String(30), nullable=False)

    site_id = Column(
        String(20),
        ForeignKey("sites.site_id"),
        nullable=True
    )

    site = relationship("Site", back_populates="assets")