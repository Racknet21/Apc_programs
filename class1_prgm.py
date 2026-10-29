class BankAccount:
    count = 0

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

        BankAccount.count = BankAccount.count + 1
        self.account_number = BankAccount.count

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Amount deposited successfully")
        else:
            print("Enter a valid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            other_account.balance = other_account.balance + amount
            print("Transfer successful")
        else:
            print("Insufficient balance or invalid amount")


# Creating two objects
account1 = BankAccount("Rahul")
account2 = BankAccount("Priya")

# Deposit money
account1.deposit(5000)
account2.deposit(3000)

# Withdraw money
account1.withdraw(1000)

# Transfer money
account1.transfer(2000, account2)

# Display balances
account1.display_balance()
account2.display_balance()
