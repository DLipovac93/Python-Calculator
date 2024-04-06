operator = input("Enter a operator (+ - x / ^): ")
num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Nubmer: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "x":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
elif operator == "^":
    result = num1 ^ num2
else :
    print(f"{operator} is not a vaild operator")