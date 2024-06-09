from bank import Bank
from admin import Admin

bank = Bank()
admin = Admin(bank)

admin.create_account("Ripon", "ripon@email.com", "Gangni, Meherpur", "Savings")
admin.create_account("Shahin", "shahin@email.com", "Alamdanga, Chuadanga", "Current")
admin.create_account("Shihab", "shihab@email.com", "Mirpur, Kushtia", "Savings")

def admin_menu():
    user_name = input("Enter admin user name: ")
    password = input("Enter your admin password: ")

    if user_name == "admin" and password == "1234":
        while True:
            print("\n<<<<<<------------------------>>>>>>")
            print("\n>>>>>---Chose an option below---<<<<<\n")
            print("1. Create Account")
            print("2. Delete Account")
            print("3. View All Accounts")
            print("4. Check Total Available Balance")
            print("5. Check Total Loan Amount")
            print("6. Toggle Loan Feature")
            print("7. Back to Main Menu")
            print("<<<<<<------------------------>>>>>>")

            choice = int(input("\nEnter option: "))
            print("\n")

            if choice == 1:
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                address = input("Enter Address: ")
                account_type = input("Enter Account Type (Savings/Current): ")
                admin.create_account(name, email, address, account_type)

            elif choice == 2:
                account_number = input("Enter account number to delete: ")
                admin.delete_account(account_number)

            elif choice == 3:
                admin.view_all_account()

            elif choice == 4:
                print(f"Total Available Balance: {admin.total_available_balance()}")

            elif choice == 5:
                print(f"Total Loan Amount: {admin.total_loan()}")

            elif choice == 6:
                status = input("Enter 'on' to enable loan feature, 'off' to disable: ")
                if status == 'on':
                    admin.toggle_loan_feature(True)
                elif status == 'off':
                    admin.toggle_loan_feature(False)
                else:
                    print("Invalid input. Please enter 'on' or 'off'.")

            elif choice == 7:
                print("Exiting System...")
                break

            else:
                print("Invalid Option! Please chose a valid option.")
    else:
        print("Invalid admin information!")

def customer_menu():
    while True:
        print("\n<<<<<<------------------------>>>>>>")
        print("\n>>>>>---Chose an option below---<<<<<\n")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Take Loan")
        print("7. Transfer Money")
        print("8. Back to Main Menu")
        print("<<<<<<------------------------>>>>>>")

        choice = int(input("\nEnter option: "))
        print("\n")

        if choice == 1:
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            account_type = input("Enter Account Type (Savings/Current): ")
            admin.create_account(name, email, address, account_type)

        elif choice == 2:
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter amount to deposit: "))
            if account_number in bank.accounts:
                bank.accounts[account_number].deposit(amount)
            else:
                print("Account does not exist")

        elif choice == 3:
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter amount to withdraw: "))
            if account_number in bank.accounts:
                bank.accounts[account_number].withdraw(amount)
            else:
                print("Account does not exist")

        elif choice == 4:
            account_number = input("Enter Account Number: ")
            if account_number in bank.accounts:
                print(f"Name: {bank.accounts[account_number].show_name()}")
                print(f"Balance: {bank.accounts[account_number].check_balance()}")
            else:
                print("Account does not exist")

        elif choice == 5:
            account_number = input("Enter Account Number: ")
            if account_number in bank.accounts:
                print("Transaction History: ")
                for entry in bank.accounts[account_number].get_transaction_history():
                    print(entry)
            else:
                print("Account does not exist")

        elif choice == 6:
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter Loan Amount: "))
            if account_number in bank.accounts:
                bank.accounts[account_number].take_loan(amount, bank)
            else:
                print("Account does not exist")

        elif choice == 7:
            from_account = input("Enter Your Account Number: ")
            to_account = input("Enter The Recipient's Account Number: ")
            amount = float(input("Enter Amount to Transfer: "))
            bank.transfer(from_account, to_account, amount)

        elif choice == 8:
            print("Exiting System...")
            break

        else:
            print("Invalid Option! Please chose a valid option.")


while True:
    print("\n^^^^^--Chose an option--^^^^^\n")
    print("Welcome!!")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")
    choice = int(input("Enter Your Choice: "))
    print("⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇")
    if choice == 1:
        admin_menu()
    elif choice == 2:
        customer_menu()
    elif choice == 3:
        print("Exiting System...")
        break
    else:
        print("Invalid Option! Please chose a valid option.")