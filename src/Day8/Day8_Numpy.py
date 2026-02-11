import numpy as np 

# Zero Dimensional Array
zero_dim=np.array(10)
print("Dimension:",zero_dim.ndim)

# One Dimensional Array
b=np.array([10,20,30])
print("Dimension of b:",b.ndim)
print(b.shape)

# Two Dimensional Array
a=np.array([[1,2,3],[4,5,6]])
print("Dimension of a:",a.ndim)

result=a+b
print("Addiion of a and b:",result)

# Three Dimensional Array
arr1 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(arr1)
print("Dimension of arr1:",arr1.ndim)


#Vectorized vs Loop example

arr=np.random.rand(1,10)
print(arr)
squared=arr**2
print(squared)


# Reshaping the array using reshape()
arr2=np.arange(12)
print(arr2)
reshaped=arr2.reshape(3,4)
print(reshaped)


# Stacking arrays Vertically and horizontally
a1=np.array([[1,2]])
b1=np.array([[3,4]])
vstacked=np.vstack((a1,b1))
print("Vertical Stacking:",vstacked)
hstacked=np.hstack((a1,b1))
print("Horizontal Stacking:",hstacked)


# Statistical functions in Numpy
import numpy as np
data=np.array([[10,20,30],[40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))
print(np.mean(data,axis=1))
A = np.array([[1, 2],[3, 4]])
B = np.array([[5, 6],[7, 8]])
print(np.dot(A, B))
arr4=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr4[1,0,2])
arr5=np.array([1,2,3,4,5,6,7])
print(arr5[1:5])
arr6=np.arange(40,55,3)
print(arr6)
arr7=np.arange(1,17).reshape(4,4)
print(arr7)
arr9=np.arange(0,12,2)
print("Shape before shaping")
print(arr9)
arr8=arr9.reshape(1,2,3)
print("Shape after reshape:",arr8.shape)
print(arr8)
A1=np.linspace(0,2,5)
print(A1)
A2=np.random.rand(2,3)
print(A2)
A3=np.random.uniform(20,20,size=(2,2))
print(A3)
print(A3.dtype)
arr=np.array([1.2,2.8,-3.7])
print(np.floor(arr))
print(np.ceil(arr))
print(np.trunc(arr))
print(np.round(arr))

#Array Operations & Broadcasting
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)  # Element-wise addition
print("Multiplication by scalar:", a * 2)
print("Element-wise multiplication:", a * b)
print("Mean of array a:", np.mean(a))


# Linear Algebra in Numpy
A = np.array([[1, 2],[3, 4]])
v = np.array([5, 6])

result = A @ v
print(result)
B = np.array([[2, 0],[1, 2]])
print("Product of A and B:")
print(A @ B)

print("Transpose of A:",A.T)

det = np.linalg.det(A)
print("Determinant of A:",det)

inv = np.linalg.inv(A)
print("Inverse of A:",inv)



