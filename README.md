# WAX-AI Project

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

AI/ML project for WAX with a complete structure for data science and machine learning workflows.

## Project Organization

```
├── README.md          <- The top-level README for developers using this project.
│
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `01-jn-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         src and configuration for tools like ruff
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
└── src                <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py          <- Code to run model inference with trained models
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

## Getting Started

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Activate the virtual environment:

   ```bash
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Start working with notebooks or scripts in `src/`

## Project Workflow

1. **Data Collection**: Add raw data to `data/raw/`
2. **Data Processing**: Use `src/dataset.py` to load and process data
3. **Feature Engineering**: Create features in `src/features.py`
4. **Model Training**: Train models using `src/modeling/train.py`
5. **Model Evaluation**: Make predictions with `src/modeling/predict.py`
6. **Visualization**: Create plots with `src/plots.py`
7. **Experimentation**: Use Jupyter notebooks in `notebooks/` for exploration

---
