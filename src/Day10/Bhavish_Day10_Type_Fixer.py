import pandas as pd
df = pd.read_csv("customer_orders.csv")
print("Initial Data Types:\n")
print(df.dtypes)
df = df.rename(columns={"OrderDate": "Date"})
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce", format="mixed")
print("\nData Types After Cleaning:\n")
print(df.dtypes)