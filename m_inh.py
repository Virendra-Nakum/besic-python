class BankAccount:

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transaction = []

    def display(self):
        print("-" * 40)
        print(f"Account Number : {self.acc_no}")
        print(f"Customer Name  : {self.name}")
        print(f"Balance        : ₹{self.balance}")
        print("-" * 40)


class BankManagement:

    def __init__(self):
        self.accounts = []

    # ---------------- CREATE ACCOUNT ----------------

    def create_account(self):

        try:
            acc_no = int(input("Enter Account Number : "))

            for account in self.accounts:
                if account.acc_no == acc_no:
                    print("Account Already Exists.")
                    return

            name = input("Enter Customer Name : ")

            balance = float(input("Enter Opening Balance : "))

            if balance < 0:
                print("Balance Cannot Be Negative")
                return

            new_account = BankAccount(acc_no, name, balance)

            self.accounts.append(new_account)

            print("Account Created Successfully.")

        except ValueError:
            print("Invalid Input!")

    # ---------------- VIEW ALL ----------------

    def view_accounts(self):

        if len(self.accounts) == 0:
            print("No Account Found.")
            return

        for account in self.accounts:
            account.display()

    # ---------------- SEARCH ----------------

    def search_account(self):

        try:
            acc_no = int(input("Enter Account Number : "))

            for account in self.accounts:

                if account.acc_no == acc_no:
                    print("Account Found")
                    account.display()
                    return

            print("Account Not Found.")

        except ValueError:
            print("Invalid Input!")

# ---------------- UPDATE ----------------

def update_account(self):

    try:
        acc_no = int(input("Enter Account Number : "))

        for account in self.accounts:

            if account.acc_no == acc_no:

                account.name = input("Enter New Name : ")

                print("Account Updated Successfully.")
                return

        print("Account Not Found.")

    except ValueError:
        print("Invalid Input")


# ---------------- DELETE ----------------

def delete_account(self):

    try:
        acc_no = int(input("Enter Account Number : "))

        for account in self.accounts:

            if account.acc_no == acc_no:

                self.accounts.remove(account)

                print("Account Deleted Successfully.")
                return

        print("Account Not Found.")

    except ValueError:
        print("Invalid Input")


# ---------------- DEPOSIT ----------------

def deposit(self):

    try:
        acc_no = int(input("Enter Account Number : "))

        for account in self.accounts:

            if account.acc_no == acc_no:

                amount = float(input("Enter Deposit Amount : "))

                if amount <= 0:
                    print("Invalid Amount")
                    return

                account.balance += amount

                account.transaction.append(f"Deposit : {amount}")

                print("Deposit Successful")
                return

        print("Account Not Found.")

    except ValueError:
        print("Invalid Input")


# ---------------- WITHDRAW ----------------

def withdraw(self):

    try:
        acc_no = int(input("Enter Account Number : "))

        for account in self.accounts:

            if account.acc_no == acc_no:

                amount = float(input("Enter Withdraw Amount : "))

                if amount <= 0:
                    print("Invalid Amount")
                    return

                if amount > account.balance:
                    print("Insufficient Balance")
                    return

                account.balance -= amount

                account.transaction.append(f"Withdraw : {amount}")

                print("Withdraw Successful")
                return

        print("Account Not Found.")

    except ValueError:
        print("Invalid Input")

import numpy as np
import matplotlib.pyplot as plt

def transaction_history(self):

    try:
        acc_no = int(input("Enter Account Number : "))

        for account in self.accounts:

            if account.acc_no == acc_no:

                print("\nTransaction History")

                if len(account.transaction) == 0:
                    print("No Transactions")
                else:
                    for t in account.transaction:
                        print(t)

                return

        print("Account Not Found")

    except ValueError:
        print("Invalid Input")

def account_analysis(self):

    if len(self.accounts) == 0:
        print("No Accounts Available")
        return

    balances = np.array([account.balance for account in self.accounts])

    print("\n----- Analysis -----")
    print("Total Balance :", np.sum(balances))
    print("Average Balance :", np.mean(balances))
    print("Maximum Balance :", np.max(balances))
    print("Minimum Balance :", np.min(balances))

def balance_graph(self):

    if len(self.accounts) == 0:
        print("No Accounts Available")
        return

    names = [account.name for account in self.accounts]
    balances = [account.balance for account in self.accounts]

    plt.figure(figsize=(8,5))
    plt.bar(names, balances)
    plt.title("Customer Balance Report")
    plt.xlabel("Customer")
    plt.ylabel("Balance")
    plt.grid(True)
    plt.show()

class BankAccount:

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance
        self.transaction = []

def get_balance(self):
    return self.__balance

def deposit(self, amount):
    self.__balance += amount
    self.transaction.append(f"Deposit : {amount}")

def withdraw(self, amount):

    if amount > self.__balance:
        return False

    self.__balance -= amount
    self.transaction.append(f"Withdraw : {amount}")
    return True
def display(self):

    print("-"*40)
    print("Account Number :", self.acc_no)
    print("Customer Name  :", self.name)
    print("Balance        :", self.__balance)
    print("-"*40)
# balances = np.array([account.get_balance() for account in self.accounts])
# balances = [account.get_balance() for account ]

while True:

    print("\n====== BANK MANAGEMENT SYSTEM ======")

    print("1.Create Account")
    print("2.View Accounts")
    print("3.Search Account")
    print("4.Update Account")
    print("5.Delete Account")
    print("6.Deposit")
    print("7.Withdraw")
    print("8.Transaction History")
    print("9.Account Analysis")
    print("10.Balance Graph")
    print("11.Exit")

    choice = input("Enter Choice : ")
    bank = BankManagement()

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.view_accounts()

    elif choice == "3":
        bank.search_account()


    elif choice == "4":
        bank.update_account()

    elif choice == "5":
        bank.delete_account()

    elif choice == "6":
        bank.deposit()

    elif choice == "7":
        bank.withdraw()
 
    elif choice == "8":
        bank.transaction_history()

    elif choice == "9":
        bank.account_analysis()

    elif choice == "10":
        bank.balance_graph()

    elif choice == "11":
        print("Thank You")
        

    # if choice == "1":
    #     bank.create_account()

    # elif choice == "2":
    #     bank.view_accounts()

    # elif choice == "3":
    #     bank.search_account()

    # elif choice == "4":
    #     bank.update_account()

    # elif choice == "5":
    #     bank.delete_account()

    # elif choice == "6":
    #     bank.deposit()

    # elif choice == "7":
    #     bank.withdraw()

    # elif choice == "8":
    #     bank.transaction_history()

    # elif choice == "9":
    #     bank.account_analysis()

    # elif choice == "10":
    #     bank.balance_graph()

    # elif choice == "11":
    #     print("Thank You")
    #     break

    # else:
    #     print("Invalid Choice")