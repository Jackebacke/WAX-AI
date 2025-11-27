# WAX-AI: Ski Wax Analysis with Machine Learning

AI/ML system for analyzing ski glide wax performance using comparative testing and machine learning.

## Project Overview

WAX-AI helps cross-country skiers optimize wax selection by tracking comparative ski tests and using machine learning to recommend the best wax for given snow and weather conditions.

### How It Works

1. **Comparative Testing**: Test two skis side-by-side with different waxes, measure the distance between them after gliding
2. **Data Collection**: Record weather conditions, snow characteristics, and test results
3. **ML Analysis**: Train models on historical data to predict which wax performs best
4. **Recommendations**: Get wax suggestions for current conditions based on past performance

## Project Structure

```
app/
├── config.py              # Application configuration
├── data/
│   ├── database/          # Database connection and initialization
│   │   ├── connection.py  # Database engine setup
│   │   ├── session.py     # Session management
│   │   └── init_db.py     # Database initialization CLI
│   └── data_types/        # SQLAlchemy ORM models
│       ├── base.py        # Base model class
│       ├── ski_model.py   # Ski model table
│       ├── wax_product.py # Wax product table
│       └── test_session.py # Test session table
├── frontend/              # Streamlit web application
├── models/                # ML model training and inference
└── notebooks/             # Jupyter notebooks for analysis
```

## Getting Started

### 1. Install Dependencies

```bash
uv sync
```

### 2. Setup PostgreSQL Database

**Option A: Local PostgreSQL (Recommended for development)**

```bash
# Install PostgreSQL (macOS with Homebrew)
brew install postgresql@16
brew services start postgresql@16

# Create database
createdb waxai_db
```

**Option B: Cloud PostgreSQL (Supabase)**

1. Sign up at [supabase.com](https://supabase.com)
2. Create a new project
3. Get connection string from project settings

### 3. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your database connection string
# For local: postgresql://yourusername@localhost:5432/waxai_db
```

### 4. Initialize Database

```bash
# Create tables
python -m app.data.database.init_db --create-tables

# Create tables with sample data
python -m app.data.database.init_db --create-tables --sample-data
```

### 5. Run Application

```bash
# Start Streamlit web app (coming soon)
streamlit run app/frontend/app.py
```

## Database Schema

### Tables

- **ski_models**: Ski brands, models, and categories
- **wax_products**: Wax products with temperature ranges and application methods
- **test_sessions**: Comparative test data with:
  - Weather conditions (temperature, humidity, wind, precipitation)
  - Snow conditions (type, age, moisture, track condition)
  - Test setup (course length, profile, method)
  - Reference and test ski/wax combinations
  - Results (distance between skis, winner)

## Usage Examples

### Add a Test Session

```python
from app.data.database.session import get_db
from app.data.data_types import TestSession
from datetime import datetime

with get_db() as db:
    test = TestSession(
        test_date=datetime.now(),
        location="Training Track",
        temperature=-5.0,
        snow_type="transformed",
        reference_ski_id=1,
        reference_wax_id=1,
        test_ski_id=1,
        test_wax_id=2,
        distance_between_skis=2.5,  # Test ski glided 2.5m farther
        test_ski_won=True,
        confidence_rating=4
    )
    db.add(test)
```

### Query Test Results

```python
from app.data.database.session import get_db
from app.data.data_types import TestSession, WaxProduct

with get_db() as db:
    # Get all tests in cold conditions
    cold_tests = db.query(TestSession).filter(
        TestSession.temperature < -5.0
    ).all()

    # Find best performing wax
    winning_tests = db.query(TestSession).filter(
        TestSession.test_ski_won == True
    ).all()
```

## Development

### Database Management

```bash
# Reset database (WARNING: deletes all data)
python -m app.data.database.init_db --reset --sample-data

# Create tables only
python -m app.data.database.init_db --create-tables
```

### Code Quality

```bash
# Run linter and formatter
ruff check app/
ruff format app/
```

## Roadmap

- [x] Database schema and models
- [x] Database initialization with sample data
- [ ] Streamlit web interface
  - [ ] Add test session form
  - [ ] View and filter historical tests
  - [ ] Charts and visualizations
- [ ] ML model development
  - [ ] Feature engineering pipeline
  - [ ] Classification model (predict winner)
  - [ ] Recommendation system
- [ ] Model evaluation and metrics
- [ ] Deployment configuration

## License

Private project

## Author

Jakob Nilsson
