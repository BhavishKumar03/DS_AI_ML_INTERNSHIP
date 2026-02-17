import pandas as pd
from sklearn.preprocessing import LabelEncoder
data={"Transmission":["Automatic","Manual","Automatic","Manual","Automatic"],
      "Color":["Red","Blue","Green","Red","Blue"]}
df=pd.DataFrame(data)
print("Original Data:")
print(df)
print("Label Encoding used for: Transmission")
le=LabelEncoder()
df["Transmission"]=le.fit_transform(df["Transmission"])
print("One-Hot Encoding used for: Color (drop_first=True applied)")
df=pd.get_dummies(df,columns=["Color"],drop_first=True)
print(df)
























