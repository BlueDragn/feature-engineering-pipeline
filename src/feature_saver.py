def save_features(df, output_path):
    """
    Save processed dataframe.
    """

    df.to_csv(output_path, index=False)