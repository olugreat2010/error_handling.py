attempts = 3
for i in range(attempts):
    try:
        a = int(input("Enter dividend: "))
        b = int(input("Enter divisor: "))
        print(f"Result: {a / b}")
        break
    except ZeroDivisionError:
        print("Cannot divide by zero. Try again.")
    except ValueError:
        print("Invalid input. Enter integers only.")
    if i == attempts - 1:
        print("Too many failed attempts. Exiting.")
