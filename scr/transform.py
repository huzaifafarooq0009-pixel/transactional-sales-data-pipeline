import pandas as pd


def transform_data(df):
    df = df.drop_duplicates()
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["order_value"] = df["quantity"] * df["price"]
    df["order_month"] = df["order_date"].dt.month
    return df


if __name__ == "__main__":
    raw_data_path = "data/raw/sales_raw.csv"
    df_raw = pd.read_csv(raw_data_path)

    df_processed = transform_data(df_raw)

    output_path = "data/processed/sales_processed.csv"
    df_processed.to_csv(output_path, index=False)

    print("Data transformation completed successfully")
    print(df_processed.head())
  #  print(f"Rows: {df_processed.shape[0]}, Columns: {df_processed.shape[1]}")



