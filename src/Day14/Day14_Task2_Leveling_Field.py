import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
data={"Age":[22,25,30,35,40,45,50],"Salary":[20000,25000,40000,50000,60000,80000,100000]}
df=pd.DataFrame(data)
print("Original Data:\n")
print(df)
standard_scaler=StandardScaler()
df_standardized=pd.DataFrame(standard_scaler.fit_transform(df),columns=df.columns)
print("\nStandardized Data (StandardScaler):\n")
print(df_standardized)
minmax_scaler=MinMaxScaler()
df_normalized=pd.DataFrame(minmax_scaler.fit_transform(df),columns=df.columns)
print("\nNormalized Data (MinMaxScaler):\n")
print(df_normalized)
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.hist(df["Salary"],bins=5,edgecolor="black")
plt.title("Before Scaling")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.grid(True)
plt.subplot(1,3,2)
plt.hist(df_standardized["Salary"],bins=5,edgecolor="black")
plt.title("After StandardScaler")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")
plt.grid(True)
plt.subplot(1,3,3)
plt.hist(df_normalized["Salary"],bins=5,edgecolor="black")
plt.title("After MinMaxScaler")
plt.xlabel("Normalized Salary (0 to 1)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()




