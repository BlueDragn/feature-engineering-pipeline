
# Engineering Log

---

## Date
10 June 2026

## Project
Feature Engineering Pipeline

## Session / Topic
Session 1 — Dataset Loading and Saving

## Objective
Initialize the project structure and verify that the dataset can be loaded and saved through the pipeline.

## Work Done
- Created the Feature Engineering Pipeline project structure.
- Downloaded the Mall Customers dataset.
- Added dataset to `data/raw/customer_data.csv`.
- Implemented `data_loader.py` to load the dataset.
- Implemented `feature_saver.py` to save processed datasets.
- Connected modules through `pipeline_runner.py`.
- Added project entry point in `main.py`.
- Successfully loaded the dataset into a pandas DataFrame.
- Successfully saved a processed copy to the `data/processed/` directory.

## Observations
- Dataset shape: `(200, 5)`
- Columns:
  - CustomerID
  - Gender
  - Age
  - Annual Income (k$)
  - Spending Score (1-100)
- Dataset contains:
  - 1 categorical feature (`Gender`)
  - 4 numerical features
- No missing values detected.
- Dataset is suitable for feature engineering exercises involving:
  - Feature creation
  - Encoding
  - Scaling
  - Customer segmentation preparation

## Changes Made
### Implemented Modules
- `data_loader.py`
- `feature_saver.py`
- `pipeline_runner.py`
- `main.py`

### Pipeline Flow

```text
customer_data.csv
        ↓
data_loader.py
        ↓
DataFrame
        ↓
feature_saver.py
        ↓
processed_customer_data.csv
```

## Challenges
- Encountered `ModuleNotFoundError: No module named 'src'`.
- Resolved by adjusting import structure and execution approach.
- Installed required dependencies (`pandas`).

## Learning Points
- A DataFrame acts as the central object flowing through the pipeline.
- Every future feature transformation will operate on the same DataFrame.
- Establishing a working load → save pipeline first reduces debugging complexity later.
- Feature Engineering Pipeline follows the same architectural pattern as previous pipeline projects:
  - Input
  - Processing
  - Output


## Next Step
Implement `feature_builder.py` and create the first engineered features:

- Age_Group
- Income_Band
- High_Income_Flag
- High_Spending_Flag

Also evaluate whether `CustomerID` should be retained or removed from the feature set.


