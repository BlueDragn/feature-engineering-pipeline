from sklearn.preprocessing import MinMaxScaler

def scale_features(df):

    scaler = MinMaxScaler()

    numeric_columns = [
        "Age",
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]

    df[numeric_columns] = scaler.fit_transform(
        df[numeric_columns]
    )
    return df