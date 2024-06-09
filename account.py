class Account:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print(f"Deposited {amount} to account {self.account_number}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
            return False
        self.balance -= amount
        self.transaction_history.append(f"Withdrew {amount}")
        print(f"Withdrew {amount} from account {self.account_number}")
        return True

    def check_balance(self):
        return self.balance

    def show_name(self):
        return self.name

    def get_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount, bank):
        if bank.loan_feature_on:
            if self.loan_count >= 2:
                print("Loan limit exceeded")
            else:
                self.balance += amount
                bank.total_loan_amount += amount
                self.loan_count += 1
                self.transaction_history.append(f"Took loan of {amount}")
                print(f"Loan of {amount} taken, total loans: {self.loan_count}")
        else:
            print("Loan feature is currently disable")