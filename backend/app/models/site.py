from sqlalchemy import Column, Float, String
from sqlalchemy.orm import relationship

from app.database import Base


class Site(Base):
    __tablename__ = "sites"

    site_id = Column(String(20), primary_key=True)
    site_name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    assets = relationship("Asset", back_populates="site")

    operators = relationship("Operator", back_populates="site")