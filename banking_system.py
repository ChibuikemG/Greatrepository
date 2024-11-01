from abc import ABC, abstractmethod

# Base class
class BankAccount(ABC):
    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self._balance = 0  # Encapsulated balance (private attribute)

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self._balance += amount
        print(f"Deposited ${amount:.2f}. New balance is ${self._balance:.2f}.")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds.")
            return
        self._balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance is ${self._balance:.2f}.")

    def get_balance(self):
        return self._balance

    def display_balance(self):
        print(f"Balance for {self.account_type()} Account {self.account_number}: ${self._balance:.2f}")

# Subclass for Checking Account
class CheckingAccount(BankAccount):
    def account_type(self):
        return "Checking"

# Subclass for Savings Account
class SavingsAccount(BankAccount):
    def account_type(self):
        return "Savings"

    # Overridden withdraw method with a limitation
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds in savings account.")
            return
        if amount > 500:
            print("Cannot withdraw more than $500 from savings at once.")
            return
        self._balance -= amount
        print(f"Withdrew ${amount:.2f} from Savings. New balance is ${self._balance:.2f}.")

# User class to manage users of the bank
class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_type, account_number):
        if account_type.lower() == "checking":
            account = CheckingAccount(account_number, self.name)
        elif account_type.lower() == "savings":
            account = SavingsAccount(account_number, self.name)
        else:
            print("Invalid account type.")
            return
        self.accounts[account_number] = account
        print(f"{account_type.capitalize()} Account {account_number} created for {self.name}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

# Main Functionality
def main():
    user = User(input("Enter user name: "))
    
    while True:
        print("\nBanking System Menu")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Balance")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            account_type = input("Enter account type (Checking/Savings): ")
            account_number = input("Enter new account number: ")
            user.create_account(account_type, account_number)
        
        elif choice == "2":
            account_number = input("Enter account number to deposit: ")
            account = user.get_account(account_number)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")
        
        elif choice == "3":
            account_number = input("Enter account number to withdraw from: ")
            account = user.get_account(account_number)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")
        
        elif choice == "4":
            account_number = input("Enter account number to check balance: ")
            account = user.get_account(account_number)
            if account:
                account.display_balance()
            else:
                print("Account not found.")
        
        elif choice == "5":
            print("Exiting the Banking System.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
