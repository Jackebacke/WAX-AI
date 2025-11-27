"""Database connection management."""

import os
from typing import Optional

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

# Load environment variables
load_dotenv()


def get_database_url() -> str:
    """Get database URL from environment variable.

    Returns:
        PostgreSQL connection string

    Raises:
        ValueError: If DATABASE_URL is not set
    """
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError(
            "DATABASE_URL environment variable not set. "
            "Please create a .env file with DATABASE_URL (see .env.example)"
        )
    return database_url


def create_db_engine(connection_string: Optional[str] = None, echo: bool = False) -> Engine:
    """Create SQLAlchemy database engine.

    Args:
        connection_string: Optional PostgreSQL connection string.
            If not provided, reads from DATABASE_URL environment variable.
        echo: If True, log all SQL statements

    Returns:
        SQLAlchemy Engine instance
    """
    if connection_string is None:
        connection_string = get_database_url()

    engine = create_engine(connection_string, echo=echo)
    return engine


# Global engine instance (lazy loaded)
_engine: Optional[Engine] = None


def get_engine(echo: bool = False) -> Engine:
    """Get or create the global database engine.

    Args:
        echo: If True, log all SQL statements

    Returns:
        SQLAlchemy Engine instance
    """
    global _engine
    if _engine is None:
        _engine = create_db_engine(echo=echo)
    return _engine
