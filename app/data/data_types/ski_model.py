"""Ski model database table."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship

from app.data.data_types.base import Base


class SkiModel(Base):
    """Ski model information."""

    __tablename__ = "ski_models"

    id = Column(Integer, primary_key=True)
    brand = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    year = Column(Integer, nullable=True)
    category = Column(String(50), nullable=True)  # e.g., "classic", "skate", "racing"
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships - one ski model can be used in many tests
    test_sessions_reference = relationship(
        "TestSession",
        back_populates="reference_ski_model",
        foreign_keys="TestSession.reference_ski_id",
    )
    test_sessions_test = relationship(
        "TestSession", back_populates="test_ski_model", foreign_keys="TestSession.test_ski_id"
    )

    def __repr__(self):
        return f"<SkiModel(brand='{self.brand}', model='{self.model}', year={self.year})>"
