"""Wax product database table."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import relationship

from app.data.data_types.base import Base


class WaxProduct(Base):
    """Wax product information."""

    __tablename__ = "wax_products"

    id = Column(Integer, primary_key=True)
    brand = Column(String(100), nullable=False)
    product_name = Column(String(100), nullable=False)
    wax_type = Column(String(50), nullable=False)  # e.g., "glide", "kick", "universal"
    temp_range_low = Column(Float, nullable=True)  # Celsius
    temp_range_high = Column(Float, nullable=True)  # Celsius
    color_code = Column(String(50), nullable=True)  # e.g., "red", "blue", "yellow"
    application_method = Column(String(50), nullable=True)  # e.g., "hot wax", "rub-on"
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    test_sessions_reference = relationship(
        "TestSession",
        back_populates="reference_wax",
        foreign_keys="TestSession.reference_wax_id",
    )
    test_sessions_test = relationship(
        "TestSession", back_populates="test_wax", foreign_keys="TestSession.test_wax_id"
    )

    def __repr__(self):
        return f"<WaxProduct(brand='{self.brand}', product='{self.product_name}', type='{self.wax_type}')>"
