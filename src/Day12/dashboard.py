import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]
months = [1, 2, 3, 4, 5]
revenue = [200, 400, 350, 500, 650]
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Category Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.subplot(1, 2, 2)
plt.plot(months, revenue, marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()







