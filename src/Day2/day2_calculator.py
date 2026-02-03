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