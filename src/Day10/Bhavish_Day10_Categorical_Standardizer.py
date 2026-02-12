import pandas as pd

df = pd.read_csv("customer_orders.csv")
print("Shape before cleaning:", df.shape)
df["Location"] = df["Location"].str.strip().str.title()
print("\nUnique Locations After Cleaning:")
print(df["Location"].unique())
df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)