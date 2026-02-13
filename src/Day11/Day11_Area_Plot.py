import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.fill_between(x, y, label="Area")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Area Plot Example")
plt.grid(True)
plt.legend()
plt.show()
















