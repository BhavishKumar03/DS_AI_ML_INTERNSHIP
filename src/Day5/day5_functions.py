#simple function to greet
def greet():
    print("Hello, welcome to the Internet of Things course!")
greet()

#function to add two numbers
def add_numbers(a, b):
    return a + b
result = add_numbers(5,3)
print("The sum is:", result)

#demonstrating variable scope
x=10
def show_value():
    x=5
    print(x)
show_value()
print(x)

vegetable="carrot"
def print_message():
    fruit="apple"
    animal="dog"
    print("Vegetable:", vegetable)
    print("Fruit:", fruit)
print_message()
#print("Animal:", animal) # This will cause an error because 'animal' is not defined in this scope

import math
import random
print(math.sqrt(16))
print(random.randint(1, 10))
print(random.uniform(0, 1))
print(random.choice(['apple', 'banana', 'cherry']))
print(random.sample([1, 2, 3, 4, 5], 3))
print(random.shuffle([1, 2, 3, 4, 5]))
print(random.randrange(1, 10, 2))
print(random.seed(42))
print(random.random())

#Example of NameError
#print(b) # This will cause a NameError because 'b' is not defined   

#hello()

#example of import error
#from math import squareroot

#example of module not found error
#import numpyyy


#Calculating area and perimeter of a rectangle
def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area, perimeter = calc_rectangle(length, width)
print(f"Area: {area}, Perimeter: {perimeter}")