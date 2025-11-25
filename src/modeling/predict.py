"""Code to run model inference with trained models."""

from pathlib import Path

import numpy as np


def load_model(filepath: str | Path) -> object:
    """Load a trained model from disk.

    Args:
        filepath: Path to the saved model

    Returns:
        Loaded model
    """
    import joblib

    model = joblib.load(filepath)
    print(f"Model loaded from {filepath}")
    return model


def predict(model, X: np.ndarray) -> np.ndarray:
    """Make predictions using a trained model.

    Args:
        model: Trained model
        X: Feature array for prediction

    Returns:
        Array of predictions
    """
    return model.predict(X)


def predict_proba(model, X: np.ndarray) -> np.ndarray:
    """Make probability predictions using a trained classifier.

    Args:
        model: Trained classification model
        X: Feature array for prediction

    Returns:
        Array of probability predictions
    """
    if hasattr(model, "predict_proba"):
        return model.predict_proba(X)
    else:
        raise AttributeError("Model does not support probability predictions")
