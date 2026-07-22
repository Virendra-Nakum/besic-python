d= {
    "tea":50,
    "bus_tikit":345,
    "launch":500
}

def add_expense():
    expense= input("enter expense:-")
    pay= input("enter amount:-")
    if expense.isalpha() and pay.isdigit() :
        expense = str(expense) 
        pay = int(pay)
        d[expense]= pay
    else:
        print("try again.")
    print(d)


def display_excpense():
    print(d)
 
def total_expense():
  print(sum(d.values()))


def search_expense():
   expense = input("enter search item:-")
   if expense in d.keys():
      print("yes, this expense avalible here.")
   else:
      print("this expense not avalible. ")

def delet_expense():
   expense = input("you can delet expense:- ")
     
   if expense in d.keys() :
      d.pop(expense)
   else :
      print("not found this expense.")
   print(d)
    
 
      

while True:
    print("==== expense Management System ====")
    print("1. Add expenses")
    print("2. View expenses")
    print("3. total expense")
    print("4. search expense")
    print("5. delet expense.")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        display_excpense()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        search_expense()
    elif choice == "5":
        delet_expense()
    elif choice == "6":
        break
    else:
      print("Invalid choice. Please try again.")


  