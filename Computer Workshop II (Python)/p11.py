import random
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction_code = self.generate_transaction_code()
            print(f"Deposit successful! Transaction code: {transaction_code}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            transaction_code = self.generate_transaction_code()
            print(f"Withdrawal successful! Transaction code: {transaction_code}")
        else:
            print("Insufficient balance or invalid amount for withdrawal.")
            
    @staticmethod
    def generate_transaction_code():
        return random.randint(1000, 9999)

account_number = "1234567890"
bank_account = BankAccount(account_number)
print(f"Account number: {bank_account.account_number}")
print(f"Initial balance: {bank_account.balance}")
bank_account.deposit(100)
print(f"Updated balance: {bank_account.balance}")
bank_account.withdraw(50)
print(f"Updated balance: {bank_account.balance}")