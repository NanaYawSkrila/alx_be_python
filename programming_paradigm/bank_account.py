class BankAccount:
    def __init__(self, initial_balance=0):
        # Make sure the attribute name matches what you use later
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Format with two decimal places
        print(f"Current Balance: ${self.account_balance:.2f}")
