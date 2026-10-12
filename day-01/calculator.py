try:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    operator = input("Enter operation:")

    if operator == "+":
       print("Result:", num1 + num2)
    elif operator == "-":
       print("Result:", num1 - num2)
    elif operator == "*":
       print("Result:", num1 * num2)
    elif operator == "/":
      if num2==0:
       print("Error: Cannot divide by zero")
      else:
       print("Result:", num1 / num2)
    else:
       print("Error: Invalid operator")

except ValueError:
    print("Please enter a valid number")
