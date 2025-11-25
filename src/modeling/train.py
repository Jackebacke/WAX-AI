"""Code to train models."""

from pathlib import Path

import numpy as np
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split

from src.config import RANDOM_SEED, TEST_SIZE


def split_data(
    X: np.ndarray, y: np.ndarray, test_size: float = TEST_SIZE, random_state: int = RANDOM_SEED
) -> tuple:
    """Split data into train and test sets.

    Args:
        X: Feature array
        y: Target array
        test_size: Proportion of dataset to include in test split
        random_state: Random seed for reproducibility

    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_model(model, X_train: np.ndarray, y_train: np.ndarray) -> object:
    """Train a machine learning model.

    Args:
        model: Model instance to train
        X_train: Training features
        y_train: Training targets

    Returns:
        Trained model
    """
    model.fit(X_train, y_train)
    return model


def evaluate_model(
    model, X_test: np.ndarray, y_test: np.ndarray, task: str = "classification"
) -> dict:
    """Evaluate a trained model.

    Args:
        model: Trained model
        X_test: Test features
        y_test: Test targets
        task: Type of task ('classification' or 'regression')

    Returns:
        Dictionary containing evaluation metrics
    """
    predictions = model.predict(X_test)

    if task == "classification":
        accuracy = accuracy_score(y_test, predictions)
        return {"accuracy": accuracy}
    else:  # regression
        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)
        return {"mse": mse, "rmse": rmse}


def save_model(model, filepath: str | Path) -> None:
    """Save trained model to disk.

    Args:
        model: Trained model to save
        filepath: Path to save the model
    """
    import joblib

    joblib.dump(model, filepath)
    print(f"Model saved to {filepath}")
