try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"Result: {result}")
except ValueError:
    print("Please enter valid integers.")
print()