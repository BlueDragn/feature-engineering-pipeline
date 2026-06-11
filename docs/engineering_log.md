
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


---
---


## Date :: 11 June 2026

## Project
Feature Engineering Pipeline

## Session / Topic
Sessions 2–4 — Feature Creation, Encoding, and Scaling

## Objective
Transform raw customer data into an ML-ready dataset through feature engineering, categorical encoding, and numerical scaling.

---

## Starting Dataset

### Dataset Shape

```text
(200, 5)
```

### Original Columns

```text
CustomerID
Gender
Age
Annual Income (k$)
Spending Score (1-100)
```

### Initial Observations

- No missing values present.
- One categorical feature (`Gender`).
- Three numerical features (`Age`, `Annual Income (k$)`, `Spending Score (1-100)`).
- `CustomerID` identified as an identifier rather than a useful feature.

---

## Session 2 — Feature Engineering

### Objective

Create new features from existing customer information.

### Features Created

#### Age_Group

```text
18–25  → Youth
26–45  → Adult
46+    → Senior
```

#### Income_Band

```text
0–40    → Low
41–80   → Medium
81+     → High
```

#### High_Income_Flag

```text
Income > 80
```

```text
1 = High Income
0 = Otherwise
```

#### High_Spending_Flag

```text
Spending Score > 60
```

```text
1 = High Spending
0 = Otherwise
```

### Additional Feature Engineering Decision

Removed:

```text
CustomerID
```

Reason:

```text
CustomerID is an identifier and does not contain useful customer behavior information.
```

### Modules Implemented

```text
feature_builder.py
```

### Learning

Feature engineering creates additional information from existing information.

Example:

```text
Age
↓
Age_Group

Annual Income
↓
Income_Band
```

---

## Session 3 — Categorical Encoding

### Objective

Convert categorical features into numerical features.

### Categorical Features Encoded

```text
Gender
Age_Group
Income_Band
```

### Encoding Method

```text
One-Hot Encoding
```

### New Features Generated

```text
Gender_Female
Gender_Male

Age_Group_Youth
Age_Group_Adult
Age_Group_Senior

Income_Band_Low
Income_Band_Medium
Income_Band_High
```

### Modules Implemented

```text
encoder.py
```

### Learning

Machine learning models cannot directly understand categories such as:

```text
Male
Female
Youth
Adult
Senior
```

Encoding converts categories into machine-readable numerical representations.

---

## Session 4 — Feature Scaling

### Objective

Normalize numerical features to a common scale.

### Scaling Method

```text
MinMaxScaler
```

### Features Scaled

```text
Age
Annual Income (k$)
Spending Score (1-100)
```

### Example

Before:

```text
Age = 19
Income = 15
Spending Score = 39
```

After:

```text
Age = 0.019231
Income = 0.000000
Spending Score = 0.387755
```

### Features Not Scaled

```text
High_Income_Flag
High_Spending_Flag
```

Reason:

```text
Already binary values (0 or 1)
```

### Modules Implemented

```text
scaler.py
```

### Learning

Scaling prevents larger numerical ranges from dominating smaller numerical ranges during model training.

---

## Final Dataset

### Final Shape

```text
(200, 12)
```

### Final Features

```text
Age
Annual Income (k$)
Spending Score (1-100)

High_Income_Flag
High_Spending_Flag

Gender_Female
Gender_Male

Age_Group_Adult
Age_Group_Senior
Age_Group_Youth

Income_Band_High
Income_Band_Medium
Income_Band_Low
```

---

## Pipeline Flow

```text
Raw Customer Dataset
        ↓
Data Loading
        ↓
Missing Value Handling
        ↓
Feature Engineering
        ↓
Categorical Encoding
        ↓
Numerical Scaling
        ↓
Processed Dataset
        ↓
Save Output
```

---

## Files Implemented

```text
data_loader.py
feature_builder.py
encoder.py
scaler.py
feature_saver.py
pipeline_runner.py
main.py
```

---

## Challenges Encountered

### Import Issues

```text
ModuleNotFoundError: No module named 'src'
```

Resolved by adjusting import structure and execution approach.

### Feature Logic Review

Age group conditions were revised to prevent overlapping ranges.

### Encoded Output Format

Initial encoding produced:

```text
True
False
```

Updated to:

```text
1
0
```

for cleaner ML-ready output.

---

## Key Learning Outcomes

### Feature Engineering

```text
Raw Data
↓
More Informative Features
```

### Encoding

```text
Categories
↓
Numbers
```

### Scaling

```text
Different Numerical Ranges
↓
Comparable Numerical Ranges
```

### Pipeline Design

```text
Input
↓
Transformation
↓
Output
```

---

## Git Commits

```bash
git commit -m "feat: implement feature engineering module"

git commit -m "feat: implement categorical feature encoding"

git commit -m "feat: implement feature scaling pipeline"
```

---

## Next Step

Project Closure:

- Clean temporary debug prints.
- Review processed dataset.
- Update README.
- Write engineering notes.
- Conduct final project review.
- Connect learnings to future ML projects and customer segmentation systems.


