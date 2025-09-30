class NegativeAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")
    print(f"Your age is {age}")
except NegativeAgeError as a:
    print(f"{a}")
except ValueError:
    print("Please enter a valid age.")
print()
