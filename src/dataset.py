"""Scripts to download or generate data."""

import pandas as pd

from src.config import PROCESSED_DATA_DIR, RAW_DATA_DIR


def load_raw_data(filename: str) -> pd.DataFrame:
    """Load raw data from the raw data directory.

    Args:
        filename: Name of the file to load

    Returns:
        DataFrame containing the raw data
    """
    filepath = RAW_DATA_DIR / filename
    return pd.read_csv(filepath)


def save_processed_data(df: pd.DataFrame, filename: str) -> None:
    """Save processed data to the processed data directory.

    Args:
        df: DataFrame to save
        filename: Name of the file to save
    """
    filepath = PROCESSED_DATA_DIR / filename
    df.to_csv(filepath, index=False)


def download_data(url: str, filename: str) -> None:
    """Download data from a URL and save to external data directory.

    Args:
        url: URL to download data from
        filename: Name to save the file as
    """
    # Implement data downloading logic here
    pass
