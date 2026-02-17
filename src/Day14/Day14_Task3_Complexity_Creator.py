import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
data={"Experience":[0,1,2,3,4,5,6,7,8,9,10],"Salary":[20000,23000,28000,36000,47000,61000,78000,98000,121000,147000,176000]}
df=pd.DataFrame(data)
X=df[["Experience"]]
y=df["Salary"]
linear_model=LinearRegression()
linear_model.fit(X,y)
y_pred_linear=linear_model.predict(X)
r2_linear=r2_score(y,y_pred_linear)
poly=PolynomialFeatures(degree=2)
X_poly=poly.fit_transform(X)
poly_model=LinearRegression()
poly_model.fit(X_poly,y)
y_pred_poly=poly_model.predict(X_poly)
r2_poly=r2_score(y,y_pred_poly)
plt.figure(figsize=(12,5))
plt.suptitle("Linear vs Polynomial Regression")
plt.subplot(1,2,1)
plt.scatter(X,y,label="Actual Data")
plt.plot(X,y_pred_linear,label="Linear Fit")
plt.title("Linear Regression Fit")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.subplot(1,2,2)
plt.scatter(X,y,label="Actual Data")
plt.plot(X,y_pred_poly,label="Polynomial Fit (Degree=2)")
plt.title("Polynomial Regression Fit (Degree=2)")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print("R² Score using Original Linear Feature:",round(r2_linear,4))
print("R² Score using Polynomial Features (degree=2):",round(r2_poly,4))
if r2_poly>r2_linear:
    print("\nPolynomial features improved the model by capturing the curve in the data.")
else:
    print("\nPolynomial features did not improve the model.")
    
    
    
    
    
    
    
    
    
    
    
    