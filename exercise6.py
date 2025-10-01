class InsufficientFundsError(Exception):
    pass
print("1.check balance")
print("2.withrawal")
balance = 10000
try:
    option=input("enter an option: ")
    if option==1:
        print(f"current bala")
    amount = float(input("Enter amount to withdraw: "))
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds.")
    balance -= amount
    print(f"Withdrawal successful! New balance: {balance}")
except ValueError as ve:
    print(f"Value Error: {ve}")
except InsufficientFundsError as ie:
    print(f"Bank Error: {ie}")
print()
