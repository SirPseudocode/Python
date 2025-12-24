operator = input("Enter an operator (+ - * /): ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if(operator == '+'):
    print(f"Result: {round(a + b,3)}")
elif(operator == '-'):
    print(f"Result: {round(a - b,3)}")
elif(operator == '*'):
    print(f"Result: {round(a * b,3)}")
elif(operator == '/'):
    print(f"Result: {round(a / b,3)}")
else:
    print(f"{operator} is invalid operator")