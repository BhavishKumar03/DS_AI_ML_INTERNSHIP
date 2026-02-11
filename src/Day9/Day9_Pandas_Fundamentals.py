import pandas as pd
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s1)
print(s2)

marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])
print(marks['Math'])
print(marks[['Math', 'Chemistry']])

scores=pd.Series([45,67,89,34,90])
passed=scores[scores>60]
print(passed)

data=pd.Series([10,None,30,None])
print(data.isnull())
print(data.fillna(0))

names=pd.Series(['Alice','bob','CHARLIE'])
res=names.str.lower()
print(res)
print(res.str.contains('a'))
print(names.str.upper())






























