class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        self.bank.delete_account(account_number)

    def view_all_account(self):
        for account_number, account in self.bank.accounts.items():
            print(f"Account Number: {account_number}, Name: {account.name}, balance: {account.balance}")

    def total_available_balance(self):
        return self.bank.total_available_balance()

    def total_loan(self):
        return self.bank.total_loan()

    def toggle_loan_feature(self, status):
        self.bank.toggle_loan_feature(status)