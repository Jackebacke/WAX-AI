"""Database session management."""

from contextlib import contextmanager
from typing import Generator

from sqlalchemy.orm import Session, sessionmaker

from app.data.database.connection import get_engine

# Session factory (lazy loaded)
_SessionLocal: sessionmaker | None = None


def get_session_factory() -> sessionmaker:
    """Get or create the session factory.

    Returns:
        SQLAlchemy sessionmaker instance
    """
    global _SessionLocal
    if _SessionLocal is None:
        engine = get_engine()
        _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return _SessionLocal


def get_session() -> Session:
    """Create a new database session.

    Returns:
        SQLAlchemy Session instance

    Note:
        Remember to close the session when done, or use get_db() context manager
    """
    SessionLocal = get_session_factory()
    return SessionLocal()


@contextmanager
def get_db() -> Generator[Session, None, None]:
    """Context manager for database sessions.

    Yields:
        SQLAlchemy Session instance

    Example:
        with get_db() as db:
            skis = db.query(SkiModel).all()
    """
    db = get_session()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
