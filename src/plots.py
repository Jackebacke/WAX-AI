"""Code to create visualizations."""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.config import FIGURES_DIR

# Set style
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


def save_figure(filename: str, dpi: int = 300) -> None:
    """Save the current figure to the figures directory.

    Args:
        filename: Name of the file to save
        dpi: Resolution of the saved figure
    """
    filepath = FIGURES_DIR / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(filepath, dpi=dpi, bbox_inches="tight")
    plt.close()


def plot_distribution(data: pd.Series, title: str = "Distribution", save: bool = False) -> None:
    """Plot distribution of a variable.

    Args:
        data: Series containing the data
        title: Title for the plot
        save: Whether to save the figure
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data, kde=True)
    plt.title(title)
    plt.xlabel(data.name)
    plt.ylabel("Frequency")

    if save:
        save_figure(f"{title.lower().replace(' ', '_')}.png")
    else:
        plt.show()


def plot_correlation_matrix(df: pd.DataFrame, save: bool = False) -> None:
    """Plot correlation matrix heatmap.

    Args:
        df: DataFrame containing numerical features
        save: Whether to save the figure
    """
    plt.figure(figsize=(12, 10))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
    plt.title("Correlation Matrix")

    if save:
        save_figure("correlation_matrix.png")
    else:
        plt.show()


def plot_training_history(history: dict, save: bool = False) -> None:
    """Plot training history (loss and metrics over epochs).

    Args:
        history: Dictionary containing training history
        save: Whether to save the figure
    """
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Plot loss
    axes[0].plot(history.get("train_loss", []), label="Train Loss")
    axes[0].plot(history.get("val_loss", []), label="Validation Loss")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Loss")
    axes[0].set_title("Training and Validation Loss")
    axes[0].legend()

    # Plot accuracy or other metric
    if "train_acc" in history:
        axes[1].plot(history["train_acc"], label="Train Accuracy")
        axes[1].plot(history.get("val_acc", []), label="Validation Accuracy")
        axes[1].set_xlabel("Epoch")
        axes[1].set_ylabel("Accuracy")
        axes[1].set_title("Training and Validation Accuracy")
        axes[1].legend()

    plt.tight_layout()

    if save:
        save_figure("training_history.png")
    else:
        plt.show()
