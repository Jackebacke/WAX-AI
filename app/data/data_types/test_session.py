"""Test session database table with embedded weather and snow conditions."""

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.data.data_types.base import Base


class TestSession(Base):
    """Comparative ski test session data."""

    __tablename__ = "test_sessions"

    id = Column(Integer, primary_key=True)
    test_date = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    location = Column(String(200), nullable=False)

    # Weather conditions (embedded)
    temperature = Column(Float, nullable=False)  # Celsius
    humidity = Column(Float, nullable=True)  # Percentage
    wind_speed = Column(Float, nullable=True)  # m/s
    precipitation = Column(
        String(50), nullable=True
    )  # e.g., "none", "light snow", "rain", "heavy snow"

    # Snow conditions (embedded)
    snow_type = Column(
        String(50), nullable=False, index=True
    )  # e.g., "new", "old", "transformed", "artificial"
    snow_age_days = Column(Integer, nullable=True)  # Days since snowfall
    snow_temperature = Column(Float, nullable=True)  # Celsius
    snow_moisture = Column(String(50), nullable=True)  # e.g., "dry", "moist", "wet"
    track_condition = Column(String(50), nullable=True)  # e.g., "firm", "soft", "icy"

    # Test setup
    test_course_length = Column(Float, nullable=False)  # meters
    course_profile = Column(
        String(50), nullable=True
    )  # e.g., "flat", "slight_incline", "downhill"
    test_method = Column(Text, nullable=True)  # Description of how test was conducted

    # Reference ski (baseline for comparison)
    reference_ski_id = Column(Integer, ForeignKey("ski_models.id"), nullable=False)
    reference_wax_id = Column(Integer, ForeignKey("wax_products.id"), nullable=False)
    reference_prep_notes = Column(Text, nullable=True)  # Scraping, structuring, etc.

    # Test ski (the one being evaluated)
    test_ski_id = Column(Integer, ForeignKey("ski_models.id"), nullable=False)
    test_wax_id = Column(Integer, ForeignKey("wax_products.id"), nullable=False)
    test_prep_notes = Column(Text, nullable=True)

    # Test results - distance measurement between skis
    distance_between_skis = Column(
        Float, nullable=False
    )  # meters (positive = test ski ahead, negative = reference ski ahead)
    test_ski_won = Column(Boolean, nullable=False)  # True if test ski glided farther
    confidence_rating = Column(Integer, nullable=True)  # 1-5 scale for test reliability

    # Additional metadata
    tester_name = Column(String(100), nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    reference_ski_model = relationship(
        "SkiModel", back_populates="test_sessions_reference", foreign_keys=[reference_ski_id]
    )
    test_ski_model = relationship(
        "SkiModel", back_populates="test_sessions_test", foreign_keys=[test_ski_id]
    )
    reference_wax = relationship(
        "WaxProduct", back_populates="test_sessions_reference", foreign_keys=[reference_wax_id]
    )
    test_wax = relationship(
        "WaxProduct", back_populates="test_sessions_test", foreign_keys=[test_wax_id]
    )

    def __repr__(self):
        winner = "test" if self.test_ski_won else "reference"
        return f"<TestSession(date={self.test_date.date()}, winner='{winner}', distance={self.distance_between_skis}m)>"
