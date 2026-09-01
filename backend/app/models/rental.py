from sqlalchemy import Column, Date, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database import Base


class Rental(Base):
    __tablename__ = "rentals"

    rental_id = Column(String(20), primary_key=True)

    customer_id = Column(
        String(20),
        ForeignKey("customers.customer_id"),
        nullable=False
    )

    asset_id = Column(
        String(20),
        ForeignKey("assets.asset_id"),
        nullable=False
    )

    start_date = Column(Date, nullable=False)
    expected_return_date = Column(Date, nullable=False)
    actual_return_date = Column(Date, nullable=True)

    status = Column(
        String(30),
        nullable=False,
        default="ACTIVE"
    )

    customer = relationship(
        "Customer",
        back_populates="rentals"
    )

    asset = relationship("Asset", back_populates="rentals")