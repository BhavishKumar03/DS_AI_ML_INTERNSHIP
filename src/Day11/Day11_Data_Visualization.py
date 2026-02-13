import matplotlib.pyplot as plt

names = ["Amit", "Sara", "John", "Priya"]
marks = [85, 90, 78,88]

plt.bar(names, marks,color="red",width=0.5)

plt.xlabel("Students")          # X-axis label
plt.ylabel("Marks")             # Y-axis label
plt.title("Student Marks")      # Title

plt.show()





plt.subplot(1, 2, 1)
plt.plot([1,2,3], [1,4,9])
plt.title("Line Plot")
plt.subplot(2, 2, 2)
plt.barh(['A','B','C'], [3,7,5])
plt.title("Bar Chart")
plt.show()


x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='*',color="green")

plt.grid(True)   # Enable grid
#plt.grid(color='blue', linestyle=':', linewidth=1)
plt.show()




x = [1,2,3,4,5]
y1 = [10,20,15,25,30]
y2 = [5,15,10,20,25]

plt.plot(x, y1, label="Product A")
plt.plot(x, y2, label="Product B")

plt.legend()
plt.show()