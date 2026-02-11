import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
missing_values = grades.isnull()
filled_grades = grades.fillna(0)
filtered_scores = filled_grades[filled_grades > 60]
print("Original Series:\n")
print(grades)
print("\nMissing Values (True = Missing):\n")
print(missing_values)
print("\nFilled Series (Missing replaced with 0):\n")
print(filled_grades)
print("\nFiltered Scores (Greater than 60):\n")
print(filtered_scores)