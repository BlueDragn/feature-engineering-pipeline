import pandas as pd

def encode_features(df):
    categorical_columns = [
        "Gender",
        "Age_Group",
        "Income_Band"
    ]
    df = pd.get_dummies(
        df,
        columns=categorical_columns
        ).astype(int)
    return df