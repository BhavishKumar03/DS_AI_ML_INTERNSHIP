import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("housing_corr.csv")
print("Dataset Loaded Successfully!")
print(df.head())
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()
high_corr_pairs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i):
        corr_value = corr_matrix.iloc[i, j]
        if abs(corr_value) > 0.8:
            high_corr_pairs.append((corr_matrix.columns[i], 
                                    corr_matrix.columns[j], corr_value))
high_corr_pairs = sorted(high_corr_pairs, key=lambda x:
                         abs(x[2]), reverse=True)
print("\nTwo Highly Correlated Variable Pairs (Correlation > 0.8):")
if len(high_corr_pairs) >= 2:
    for k in range(2):
        var1, var2, value = high_corr_pairs[k]
        print(f"{k+1}) {var1} and {var2} = {value:.2f}")
elif len(high_corr_pairs) == 1:
    var1, var2, value = high_corr_pairs[0]
    print(f"Only one pair found: {var1} and {var2} = {value:.2f}")
else:
    print("No pairs found above 0.8 correlation.")
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Price"])
plt.title("Boxplot to Detect Outliers in Price")
plt.ylabel("Price")
plt.show()
Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df["Price"] < lower_bound) | (df["Price"] > upper_bound)]
print("\nOutliers in Price Column (Using IQR Method):")
print(outliers)






