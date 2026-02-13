# Line Graph
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o', label="Line Data")

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Graph Example")
plt.grid(True)
plt.legend()

plt.show()


# Bar Graph
import matplotlib.pyplot as plt

names = ["Amit", "Sara", "John", "Priya"]
marks = [85, 90, 78, 88]

plt.bar(names, marks, label="Marks")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Bar Graph Example")
plt.legend()
plt.grid(axis='y')

plt.show()


# Horizontal Bar Graph
import matplotlib.pyplot as plt

names = ["Amit", "Sara", "John", "Priya"]
marks = [85, 90, 78, 88]

plt.barh(names, marks, label="Marks")

plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Horizontal Bar Graph")
plt.legend()
plt.grid(axis='x')

plt.show()


# Pie Chart
import matplotlib.pyplot as plt

labels = ["Python", "Java", "C", "C++"]
sizes = [40, 30, 20, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart Example")

plt.show()


#Scatter Plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 25]

plt.scatter(x, y, label="Scatter Points")

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot Example")
plt.grid(True)
plt.legend()

plt.show()


# Histogram
import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 30, 30, 40, 50, 50, 60, 70]

plt.hist(data, bins=5, edgecolor="black")

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram Example")
plt.grid(axis='y')

plt.show()


# Box Plot
import matplotlib.pyplot as plt

data = [10, 20, 25, 30, 35, 40, 50, 60]

plt.boxplot(data)

plt.title("Box Plot Example")
plt.ylabel("Values")
plt.grid(True)

plt.show()


# Area Plot
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


# Stem Plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.stem(x, y)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Stem Plot Example")
plt.grid(True)

plt.show()


# Subplot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Line Graph")

plt.subplot(1, 2, 2)
plt.bar(x, y2)
plt.title("Bar Graph")

plt.tight_layout()
plt.show()