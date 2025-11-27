"""Configuration settings for WAX-AI application."""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# Machine Learning Configuration
RANDOM_SEED = 42
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.2
MIN_SAMPLES_FOR_PREDICTION = 20  # Minimum test sessions before enabling ML predictions
CONFIDENCE_THRESHOLD = 0.6  # Minimum confidence score for predictions

# Feature Engineering Categories
TEMPERATURE_BINS = [-20, -10, -5, -2, 0, 2, 5, 10]  # Temperature ranges for binning (Celsius)
SNOW_TYPE_CATEGORIES = ["new", "old", "transformed", "artificial", "mixed"]
SNOW_MOISTURE_CATEGORIES = ["dry", "moist", "wet"]
TRACK_CONDITION_CATEGORIES = ["soft", "firm", "icy", "variable"]
PRECIPITATION_CATEGORIES = ["none", "light snow", "heavy snow", "rain", "mixed"]
COURSE_PROFILE_CATEGORIES = ["flat", "slight_incline", "downhill", "varied"]

# Test Session Configuration
MAX_DISTANCE_BETWEEN_SKIS = 50.0  # Maximum reasonable distance in meters
MIN_TEST_COURSE_LENGTH = 10.0  # Minimum course length in meters
MAX_TEST_COURSE_LENGTH = 500.0  # Maximum course length in meters
CONFIDENCE_RATING_MIN = 1
CONFIDENCE_RATING_MAX = 5

# Application Settings
APP_NAME = "WAX-AI"
APP_VERSION = "0.0.1"
DEBUG = False
