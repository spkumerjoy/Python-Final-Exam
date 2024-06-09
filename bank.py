from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1000
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_on = True

    def generate_account_number(self):
        account_number = self.next_account_number
        self.next_account_number += 1
        return str(account_number)

    def create_account(self, name, email, address, account_type):
        account_number = self.generate_account_number()
        account = Account(name, email, address, account_type, account_number)
        self.accounts[account_number] = account
        print(f"Account created successfully. Account Number: {account_number}")
        return account

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} deleted successfully.")
        else:
            print("Account does not exist.")

    def total_available_balance(self):
        return sum(account.balance for account in self.accounts.values())

    def total_loan(self):
        return self.total_loan_amount

    def toggle_loan_feature(self, status):
        self.loan_feature_on = status
        print(f"Loan feature {'enable' if status else 'disable'}.")

    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts:
            print("Source account does not exist.")
            return
        if to_account not in self.accounts:
            print("Destination account does not exist.")
            return
        if self.accounts[from_account].withdraw(amount):
            self.accounts[to_account].deposit(amount)
            print(f"Transferred {amount} from {from_account} to {to_account}.")