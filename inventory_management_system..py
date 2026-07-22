d = {
    "pen":85,
    "books":55,
    "notepaed":40
}

def add_inventory():
    inventory= input("enter inventory name:-")
    stock= input("enter stock:-")
    if inventory.isalpha() and stock.isdigit() :
        inventory=str(inventory)
        stock= int(stock)
        d[inventory]=stock
    else:
        print("try again.")
    print(d)

def display_inventory():
    print(d)
 
def search_inventory():
    inventory=input("find item :-")
    if inventory in d.keys():
        print("allready avalible.")
    else:
        print("not found this inventry.")
    print(d)

def update_inventory():
    inventory=input("enter inventry:-") 
    stock=input("enter value:-") 
    if inventory.isalpha() and stock.isdigit() :
        inventory = str(inventory)
        stock=int(stock)
        d[inventory]=stock
    else:
        print("plese try again.")
    print(d)

def delet_invantory():
    inventory= input("inventry delet:-")
    if inventory in d.keys() :
        d.pop(inventory)
    else:
        print("not found.")
    print(d)



while True :
    print('=====inventory managment system=====')
    print("1,add invantory.")
    print("2,show invantory.")
    print("3,search inventory.")
    print("4,update inventory.")
    print("5,delet inventory.")
    print("6,exit...")

    choice = int(input("choice 1 to 6."))

    if choice == 1 :
        add_inventory()
    elif choice == 2 :
        display_inventory()
    elif choice == 3 :
        search_inventory()
    elif choice == 4 :
        update_inventory()
    elif choice == 5 :
        delet_invantory()
    elif choice == 6 :
        break
    else:
        print("invalide choice...")


 