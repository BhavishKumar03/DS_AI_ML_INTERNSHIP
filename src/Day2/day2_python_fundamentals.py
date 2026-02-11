# Data Types
age=21
height=5.8
name="Bhavish"
is_student=True
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

#User Input and f-Strings
name=input("Enter your name: ")
age=input("Enter your age: ")
print("Hello, " + name + " Welcome!")
message = f"My name is {name} and I am {age} years old."
print(message)
num1=10.5
res=complex(num1)
print("The complex number is:", res)

#Simple Calculator
num1=input("Enter first number: ")
num2=input("Enter second number: ")
operator=input("Enter operator (+, -, *, /): ")
if operator=='+':
    result=float(num1)+float(num2)
elif operator=='-':
    result=float(num1)-float(num2)
elif operator=='*':
    result=float(num1)*float(num2)
elif operator=='/':
    if float(num2)==0:
        result="Error: Division by zero"
    else:
        result=float(num1)/float(num2)
else:
    result="Invalid operator"
print("The result is:", result)

#Program to calculate age in 2030
name = input("Enter your name: ")
current_age = input("Enter your current age: ")
current_age = int(current_age)
age_in_2030 = current_age + 4
print(f"Hey {name}, you will be {age_in_2030} years old in 2030!")

#Program to split a bill among friends
total_bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))
share_per_person = total_bill / people
print(f"Total Bill: {total_bill}. Each person pays: {share_per_person}")
print(type(total_bill))
print(type(people))
print(type(share_per_person))

#Program to Raw Data Types Formatter
item_name = "Laptop"     
quantity = 2            
price = 499.99           
in_stock = True          
print("Item:", item_name, ", Qty:", quantity, ", Price:", price, ", Available:", in_stock)
total_cost = quantity * price
print("Total Cost:", total_cost)

