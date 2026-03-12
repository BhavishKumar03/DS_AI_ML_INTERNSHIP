# K-Nearest Neighbors (KNN) -- Explanation and Concepts

## 1. Can you explain KNN in your own words?

K-Nearest Neighbors (KNN) is a simple machine learning algorithm used
for classification and regression. It works by comparing a new data
point with existing data points in the dataset. The algorithm finds the
*K closest data points* (neighbors) based on a distance metric and makes
a prediction based on those neighbors.

For classification: - The class with the majority among the nearest
neighbors is chosen.

For regression: - The average value of the nearest neighbors is used.

KNN is called a **lazy learning algorithm** because it does not build a
model during training. Instead, it stores the dataset and performs
computations only when predictions are needed.

------------------------------------------------------------------------

## 2. Can you distinguish between parametric and instance-based models?

### Parametric Models

Parametric models summarize the dataset using a fixed number of
parameters.

Examples: - Linear Regression - Logistic Regression - Naive Bayes

Characteristics: - Training phase builds a mathematical model. - Model
size does not depend heavily on dataset size. - Faster predictions. -
May lose information due to assumptions about data distribution.

### Instance-Based Models

Instance-based models store the training data and make predictions using
similarity measures.

Example: - K-Nearest Neighbors (KNN)

Characteristics: - No explicit model is created. - Entire dataset is
stored. - Predictions are made by comparing new data with stored data. -
More flexible but computationally expensive during prediction.

------------------------------------------------------------------------

## 3. Have you manually calculated Euclidean and Manhattan distances?

### Euclidean Distance

It is the straight-line distance between two points.

Formula:

d = √((x1 - x2)² + (y1 - y2)²)

Example:

Point A = (2,3)\
Point B = (5,7)

d = √((2-5)² + (3-7)²)\
d = √(9 + 16)\
d = √25 = 5

### Manhattan Distance

It is the distance measured along grid paths (like city blocks).

Formula:

d = \|x1 - x2\| + \|y1 - y2\|

Example:

Point A = (2,3)\
Point B = (5,7)

d = \|2-5\| + \|3-7\|\
d = 3 + 4 = 7

------------------------------------------------------------------------

## 4. Did you implement KNN using scikit-learn successfully?

Yes, KNN can be easily implemented using scikit-learn.

Example Python Code:

``` python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create model
model = KNeighborsClassifier(n_neighbors=3)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
```

------------------------------------------------------------------------

## 5. Can you explain the Curse of Dimensionality?

The **Curse of Dimensionality** refers to problems that occur when the
number of features (dimensions) in a dataset increases.

Problems caused by high dimensions: - Distance between points becomes
less meaningful. - Data becomes sparse. - Algorithms like KNN become
less effective. - More computational resources are required.

Example: In low dimensions (2D or 3D), neighbors are easy to identify.\
But when dimensions increase (like 100 features), almost all points
appear equally distant.

Solutions: - Feature selection - Dimensionality reduction (PCA) -
Removing irrelevant features

------------------------------------------------------------------------

# Summary

KNN is a simple and powerful instance-based learning algorithm that
predicts outcomes by looking at the nearest data points. It relies
heavily on distance metrics like Euclidean and Manhattan distance and
can suffer from issues like the Curse of Dimensionality when working
with high-dimensional data.
