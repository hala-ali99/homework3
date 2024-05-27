# Define the BankAccount class
class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance.")

    def get_balance(self):
        return self.balance

    def change_account_holder_name(self, new_name):
        self.account_holder_name = new_name

    def display_account_details(self):
        print("Account Holder Name:", self.account_holder_name)
        print("Account Balance:", self.balance)

# Create a new bank account
account = BankAccount("John Doe")

# Display the initial account details
account.display_account_details()

# Deposit funds into the account
print("Depositing funds...")
account.deposit(1000)

# Display the updated account details
account.display_account_details()

# Withdraw funds from the account
print("Withdrawing Funds...")
account.withdraw(500)

# Display the updated account details
account.display_account_details()