'''
Encapsulation is the concept of bundling data and methods that operate on that data within a single unit, making it harder for other parts of the program to access or modify the data directly.

Properties of Encapsulation:

1. Data Hiding: The data is hidden from the outside world, and can only be accessed through the methods provided by the class.
2. Code Organization: The data and methods are organized in a single unit, making it easier to understand and maintain.

'''


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Data hiding using double underscore prefix
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

# Create a BankAccount object
account = BankAccount("123456789", 1000)

# Try to access the data directly (will raise an AttributeError)
try:
    print(account.__account_number)
except AttributeError:
    print("Cannot access account number directly")

# Access the data using the provided method
print(account.get_balance())  # Output: 1000

# Deposit money into the account
account.deposit(500)
print(account.get_balance())  # Output: 1500