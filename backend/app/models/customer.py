from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(String(20), primary_key=True)
    customer_name = Column(String(100), nullable=False)
    company_name = Column(String(150), nullable=True)
    contact = Column(String(30), nullable=True)
    email = Column(String(100), nullable=True)
    status = Column(String(30), nullable=False, default="ACTIVE")

    rentals = relationship("Rental", back_populates="customer")