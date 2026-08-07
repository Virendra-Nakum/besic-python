# bank managment System
# curd opretion

bank_account = {"dev":1234512345,
                "indrajit":1122334455,
                "bhavya":12131415,
                "virendra":1112131515
}
def add_account():
    customer= input("enter your name:-")
    account= input("enter your account number:-")

    if customer.isalpha() and account.isdigit():
        customer = str(customer)
        account=int(account)
        bank_account[customer]=account
        
    else:
        print("enter valid ditels.")
    print(bank_account)

def read_data():
    print(bank_account)

def search_account():
    account= input("find accout numbers :-")
    if account.isdigit():
         account= int(account)
    if account in bank_account.values():

        print(bank_account)
    else:
        print("No,Not avalible this person.")

def update_accont():
    customer= input("enter your name:-")
    account= input("enter your account number:-")
    
    if customer.isalpha() and account.isdigit():
            customer = str(customer)
            account=int(account)
            bank_account[customer]=account 
    else:
            print("enter valid ditels.")
    print(bank_account)

def delet_accont():
    customer= input("enter your name:-")
    if customer in bank_account():
        bank_account.pop(customer)
    else:
         print("no this person in here.")

while True:
        print("=======================CRUD OPPRECTIONS=====================")
        print("1  ADDED CUSTOMER IN BANK.")
        print("2  FIND CUSTOMER IN BANK.")
        print("3  CUSTOMER DETAILS UPDATE.")
        print("4  DELET AN ACCOUNT.")
        print("5  SHOW ALL ACCOUNT.")
        print("6  EXIT....")

        choise = input("ENTER YOUR CHOISE IN 1 TO 5:-")

        if choise == "1":
            add_account()
        elif choise == "2" :
            search_account()
        elif choise == "3" :
            update_accont()
        elif choise == "4" :
            delet_accont()
        elif choise == "5" :
            read_data()
        elif choise == "6":
             print("EXIT....")
        else:
             print("invalied choise.")
        break