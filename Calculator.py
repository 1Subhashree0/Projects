# Simple calculator using python 

operator = input("Enter an operator (+ - * /): ")
if operator in ["+", "-", "*", "/"]:
 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))
 if (operator == "+"):
    add = num1 + num2
    print(round(add))
 elif (operator == "-"):
    sub = num1 - num2
    print(round(sub))
 elif (operator == "*"):
    multiply = num1* num2
    print(round(multiply))
 elif (operator == "/"):
    divide = num1/num2
    print(round(divide))
else:
    print(f"The operator: {operator} you entered doesn't exist")


