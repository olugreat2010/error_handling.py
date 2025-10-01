try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print(f"=: {result}")
print()
