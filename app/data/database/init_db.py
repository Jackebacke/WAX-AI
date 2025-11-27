"""Database initialization script with CLI."""

import argparse
from datetime import datetime

from app.data.data_types import Base, SkiModel, TestSession, WaxProduct
from app.data.database.connection import get_engine
from app.data.database.session import get_db


def create_tables(drop_existing: bool = False):
    """Create all database tables.

    Args:
        drop_existing: If True, drop existing tables before creating
    """
    engine = get_engine()

    if drop_existing:
        print("Dropping existing tables...")
        Base.metadata.drop_all(bind=engine)
        print("Tables dropped.")

    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Tables created successfully!")


def add_sample_ski_models(db):
    """Add sample ski models to database."""
    skis = [
        SkiModel(
            brand="Fischer",
            model="Speedmax 3D",
            year=2024,
            category="skate",
            notes="High-performance racing ski",
        ),
        SkiModel(
            brand="Rossignol",
            model="X-IUM Premium",
            year=2023,
            category="classic",
            notes="World Cup level classic ski",
        ),
        SkiModel(
            brand="Atomic",
            model="Redster S9",
            year=2024,
            category="skate",
            notes="Competition skate ski",
        ),
        SkiModel(
            brand="Madshus",
            model="Race Speed",
            year=2023,
            category="classic",
            notes="Training and racing classic ski",
        ),
    ]

    for ski in skis:
        db.add(ski)
    db.commit()
    print(f"✓ Created {len(skis)} sample ski models")
    return skis


def add_sample_wax_products(db):
    """Add sample wax products to database."""
    waxes = [
        WaxProduct(
            brand="Swix",
            product_name="CH7X Blue",
            wax_type="glide",
            temp_range_low=-8,
            temp_range_high=-4,
            color_code="blue",
            application_method="hot wax",
            notes="Cold conditions glider",
        ),
        WaxProduct(
            brand="Swix",
            product_name="CH8X Red",
            wax_type="glide",
            temp_range_low=-4,
            temp_range_high=0,
            color_code="red",
            application_method="hot wax",
            notes="Medium cold conditions",
        ),
        WaxProduct(
            brand="Swix",
            product_name="CH10X Yellow",
            wax_type="glide",
            temp_range_low=0,
            temp_range_high=10,
            color_code="yellow",
            application_method="hot wax",
            notes="Warm/wet conditions",
        ),
        WaxProduct(
            brand="Toko",
            product_name="JetStream Block 2.0 Blue",
            wax_type="glide",
            temp_range_low=-10,
            temp_range_high=0,
            color_code="blue",
            application_method="rub-on",
            notes="High-fluorine racing wax",
        ),
        WaxProduct(
            brand="Start",
            product_name="LF04",
            wax_type="glide",
            temp_range_low=-6,
            temp_range_high=-2,
            color_code="violet",
            application_method="hot wax",
            notes="Low-fluorine racing wax",
        ),
        WaxProduct(
            brand="Rex",
            product_name="HF21 Green",
            wax_type="glide",
            temp_range_low=-1,
            temp_range_high=10,
            color_code="green",
            application_method="hot wax",
            notes="Warm conditions, high performance",
        ),
    ]

    for wax in waxes:
        db.add(wax)
    db.commit()
    print(f"✓ Created {len(waxes)} sample wax products")
    return waxes


def add_sample_test_sessions(db, skis, waxes):
    """Add sample test sessions to database."""
    tests = [
        TestSession(
            test_date=datetime(2025, 1, 15, 10, 30),
            location="Östersund Training Track",
            temperature=-5.0,
            humidity=65.0,
            wind_speed=2.5,
            precipitation="none",
            snow_type="transformed",
            snow_age_days=3,
            snow_temperature=-4.0,
            snow_moisture="dry",
            track_condition="firm",
            test_course_length=100.0,
            course_profile="flat",
            test_method="Side-by-side glide test, released simultaneously",
            reference_ski_id=skis[0].id,
            reference_wax_id=waxes[0].id,
            reference_prep_notes="Hot waxed, scraped, brushed with brass and nylon",
            test_ski_id=skis[0].id,
            test_wax_id=waxes[1].id,
            test_prep_notes="Hot waxed, scraped, brushed with brass and nylon",
            distance_between_skis=2.5,
            test_ski_won=True,
            confidence_rating=4,
            tester_name="Jakob Nilsson",
            notes="Red wax performed better than expected in these conditions",
        ),
        TestSession(
            test_date=datetime(2025, 1, 20, 9, 15),
            location="Östersund Training Track",
            temperature=-7.0,
            humidity=70.0,
            wind_speed=1.0,
            precipitation="light snow",
            snow_type="new",
            snow_age_days=0,
            snow_temperature=-6.0,
            snow_moisture="dry",
            track_condition="soft",
            test_course_length=100.0,
            course_profile="slight_incline",
            test_method="Side-by-side glide test on fresh track",
            reference_ski_id=skis[2].id,
            reference_wax_id=waxes[0].id,
            reference_prep_notes="Hot waxed twice, carefully scraped",
            test_ski_id=skis[2].id,
            test_wax_id=waxes[3].id,
            test_prep_notes="Rub-on application, polished with cork",
            distance_between_skis=-1.8,
            test_ski_won=False,
            confidence_rating=5,
            tester_name="Jakob Nilsson",
            notes="Blue hot wax superior to rub-on in cold new snow",
        ),
        TestSession(
            test_date=datetime(2025, 2, 5, 14, 0),
            location="Falun Stadium",
            temperature=-1.0,
            humidity=85.0,
            wind_speed=0.5,
            precipitation="none",
            snow_type="old",
            snow_age_days=7,
            snow_temperature=-0.5,
            snow_moisture="moist",
            track_condition="firm",
            test_course_length=150.0,
            course_profile="flat",
            test_method="Timed runs, averaged over 3 attempts",
            reference_ski_id=skis[1].id,
            reference_wax_id=waxes[1].id,
            reference_prep_notes="Standard prep, brass brush finish",
            test_ski_id=skis[3].id,
            test_wax_id=waxes[2].id,
            test_prep_notes="Hot wax, plastic scraper, fine bronze brush",
            distance_between_skis=3.2,
            test_ski_won=True,
            confidence_rating=4,
            tester_name="Jakob Nilsson",
            notes="Yellow wax clearly better in warm, moist conditions",
        ),
    ]

    for test in tests:
        db.add(test)
    db.commit()
    print(f"✓ Created {len(tests)} sample test sessions")


def populate_sample_data():
    """Populate database with sample data."""
    print("\nAdding sample data...")
    with get_db() as db:
        skis = add_sample_ski_models(db)
        waxes = add_sample_wax_products(db)
        add_sample_test_sessions(db, skis, waxes)
    print("✓ Sample data populated successfully!")


def main():
    """CLI entry point for database initialization."""
    parser = argparse.ArgumentParser(
        description="Initialize WAX-AI database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create tables only
  python -m app.data.database.init_db --create-tables

  # Create tables and add sample data
  python -m app.data.database.init_db --create-tables --sample-data

  # Reset database (drops and recreates)
  python -m app.data.database.init_db --reset --sample-data
        """,
    )
    parser.add_argument("--create-tables", action="store_true", help="Create database tables")
    parser.add_argument("--sample-data", action="store_true", help="Populate with sample data")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Drop existing tables and recreate (WARNING: deletes all data!)",
    )

    args = parser.parse_args()

    if not any([args.create_tables, args.sample_data, args.reset]):
        parser.print_help()
        return

    try:
        if args.reset:
            response = input(
                "\n⚠️  WARNING: This will delete ALL data in the database. Are you sure? (yes/no): "
            )
            if response.lower() != "yes":
                print("Aborted.")
                return
            create_tables(drop_existing=True)
        elif args.create_tables:
            create_tables(drop_existing=False)

        if args.sample_data:
            populate_sample_data()

        print("\n✅ Database initialization complete!")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
