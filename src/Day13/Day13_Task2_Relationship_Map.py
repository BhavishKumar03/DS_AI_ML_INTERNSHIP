import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("housing_features.csv")

print("Dataset Loaded Successfully!")
print(df.head())

plt.figure(figsize=(8, 5))
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("Scatter Plot: SquareFootage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x="City", y="Price", data=df)
plt.title("Boxplot: City vs Price")
plt.xlabel("City")
plt.ylabel("Price")
plt.grid(True)
plt.show()


print("\nObservation:")
print("As SquareFootage increases, Price seems to increase.")



