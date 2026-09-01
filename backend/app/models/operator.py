from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database import Base


class Operator(Base):
    __tablename__ = "operators"

    operator_id = Column(String(20), primary_key=True)
    name = Column(String(100), nullable=False)
    contact = Column(String(30), nullable=True)
    status = Column(String(30), nullable=False, default="ACTIVE")

    site_id = Column(
        String(20),
        ForeignKey("sites.site_id"),
        nullable=True
    )

    site = relationship("Site", back_populates="operators")