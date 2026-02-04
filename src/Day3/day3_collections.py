numbers=[10,20,30,40]
coordinates=(5,10)
print(numbers)
print(coordinates)


a=[100,200,300,400,500]
print(a[-3:-1])
print(a[1:5:2])
print(a[-5:-1:2])

a.pop()
print(a)
a.sort(reverse=True)
print(a)
a.append(600)
print(a)
a.insert(2,700)
print(a)
a.remove(200)
print(a)
a.sort()
print(a)
a.reverse()
print(a)

# Task 1: The Inventory Manager Code
inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print("Current Inventory:", inventory)
inventory.append("Eggs")
inventory.remove("Bananas")
inventory.sort()
print("Final Updated Inventory:", inventory)

# Task 2: The Data Slicer Code  
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])
afternoon_peak = temperatures[3:6]
print("Afternoon Peak Readings:", afternoon_peak)
last_three_hours = temperatures[-3:]
print("Last 3 Hours Readings:", last_three_hours)

# Task 3: The Immutable Config Code
screen_res = (1920, 1080)
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")
#screen_res[0] = 1280   #  TypeError: 'tuple' object does not support item assignment
print("Tuples cannot be modified!")

