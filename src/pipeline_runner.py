from data_loader import load_data
from feature_saver import save_features
from feature_builder import build_features
from encoder import encode_features
from scaler import scale_features

def run_pipeline():
    input_path = "data/raw/Mall_Customers.csv"
    output_path = "data/processed/processed_customer_data.csv"

    # Load the data
    df = load_data(input_path)

    df = build_features(df)
    df = encode_features(df)
    df = scale_features(df)

    print("\nDataset loaded successfully.")
    print(f"Dataset shape: {df.shape}")


    print(df.head())
    print(df.columns.tolist())


    # Save the processed data
    save_features(df, output_path)

    print(f"\nDataset Saved To: {output_path}.")

