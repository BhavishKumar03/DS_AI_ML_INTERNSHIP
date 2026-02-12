import pandas as pd
df = pd.read_csv("customer_orders.csv")
print("Shape before cleaning:", df.shape)
print("\nMissing Values Report:")
print(df.isna().sum())
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
for col in numeric_cols:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)
df = df.drop_duplicates()
print("\nShape after cleaning:", df.shape)