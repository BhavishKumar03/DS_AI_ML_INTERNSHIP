import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing.csv")
print("Dataset Loaded Successfully!")
print(df.head())

plt.figure(figsize=(8, 5))
sns.histplot(df["Price"], kde=True, bins=8)
plt.title("Histogram with KDE - Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()
print("\nSkewness of Price:", skewness)
print("Kurtosis of Price:", kurtosis)


plt.figure(figsize=(8, 5))
sns.countplot(x="City", data=df)
plt.title("Count Plot - City Frequency")
plt.xlabel("City")
plt.ylabel("Count")
plt.grid(True)
plt.show()


most_frequent_city = df["City"].value_counts().idxmax()
print("\nMost Frequent City:", most_frequent_city)





