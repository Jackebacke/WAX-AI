"""Code to create features for modeling."""

import pandas as pd
from sklearn.preprocessing import StandardScaler


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create features from raw data.

    Args:
        df: Input DataFrame

    Returns:
        DataFrame with engineered features
    """
    # Implement feature engineering logic here
    df_features = df.copy()

    return df_features


def scale_features(df: pd.DataFrame, columns: list[str]) -> tuple[pd.DataFrame, StandardScaler]:
    """Scale features using StandardScaler.

    Args:
        df: Input DataFrame
        columns: List of columns to scale

    Returns:
        Tuple of (scaled DataFrame, fitted scaler)
    """
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[columns] = scaler.fit_transform(df[columns])

    return df_scaled, scaler
