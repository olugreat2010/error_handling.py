filename = input("Enter filename to read: ")
try:
    with open(filename, "r") as g:
        file = g.read()
except FileNotFoundError:
    print("Error: File not found!")
else:
    print("Content:")
    print(file)
    print("File read successfully!")
print()
