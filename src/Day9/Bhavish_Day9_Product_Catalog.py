import pandas as pd
products = pd.Series([700, 150, 300], index=["Laptop", "Mouse", "Keyboard"])
laptop_price = products["Laptop"]
first_two = products.iloc[:2]
print("Full Series:\n", products)
print("\nPrice of Laptop:", laptop_price)
print("\nFirst Two Products:\n", first_two)