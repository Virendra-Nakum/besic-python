
l= ["python","java","ccc"]

def add_book():
    m=input("enter your boook name:-")

    l.append(m)
    print(l)

def display_book():
    print(l)

def search_book():
    v=input("find book.")
    
    if v in l:
        print("yes, this book is show ")
    else:
        print("not found this book, try again..")


def issue_book():
    v = input("Enter book name: ").lower()

    if v in l:
        print("Book not Issued.")
    else:
        print("Book not found.")


def return_book():
    v = input("Enter book name: ").lower()

    if v in l:
        print("Book returned.")
    else:
        print("Book not found.")
    print(l)

while True:
    print("==== Library Management System ====")
    print("1. Add Book")
    print("2. Display Book")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")


      #####  use dictnory  #####


books ={
    "book1":"python",
    "book2":"java",
    "book3":"ccc",
    "book4":"html"
}

def add_book():
    m=input("enter your boook name:-")
    books["book5"] = m
    print(books)


def view_books():
    print(books)


def search_books():
    m=input("find book.")
    
    if m in books.values() :
        print("yes , this book is avalible this dict...")
    else:
        print("not found this book , plese try again.")


def issue_books():
    m=input("enter book name: ")

    if m in  books.values() :
        print("no issue this book.")
    else :
        print("book not found, try again.")


def return_books():
    m = input("Enter book name: ").lower()

    if m in books.values():
        print("Book returned.")
    else:
        print("Book not found.")
    print(books)


while True:
    print("==== Library Management System ====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_books()
    elif choice == "4":
        issue_books()
    elif choice == "5":
        return_books()
    elif choice == "6":
        break
    else:
      print("Invalid choice. Please try again.")

      

      #####  employees management sytem   #####



d= {
    "laxman": 1512,
    "ram":1212,
    "syam":1412,
    'hanuman':1215
}

def add_employees():
    m= input("enter employee name:-").isalpha()
    v= input("enter employee ID:-").isdigit()
    d[m]=v
    print(d)

def dispaly_employees():
    print(d)
 
def search_employees():
    m= input("find employeee.")
    if m in d.keys() :
        print("yes , employee are avalible here..")
    else:
        print("not found , tihs employee.")
    
def update_emploees():
    m= input("enter update name:-").isalpha()
    V= input("enter empolyees ID:-").isdigit()
    d[m]=V
    print(d)
 

def delet_employees():
    v=input("delet an empolyees:-")

    if v in d :
       d.pop(v)
    else:
        print("employees not fount...")
    print(d)
 
 
while True:
    print("==== employees Management System ====")
    print("1. Add employees")
    print("2. View employees")
    print("3. Search employees")
    print("4. update employees")
    print("5. delet employees.")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employees()
    elif choice == "2":
        dispaly_employees
    elif choice == "3":
        search_employees()
    elif choice == "4":
        update_emploees()
    elif choice == "5":
        delet_employees()
    elif choice == "6":
        break
    else:
      print("Invalid choice. Please try again.")





      #####  expense mangement system  #####



d= {
    "tea":50,
    "bus_tikit":345,
    "launch":500
}

def add_expense():
    m= input("enter expense:-").isalpha()
    v= input("enter amount:-").isdigit()

    d[m]= v
    print(d)


def display_excpense():
    print(d)
 
def total_expense():
  print(sum(d.values()))


def search_expense():
   m= input("enter search item:-").isalpha()
   if m in d :
      print("yes, this expense avalible here.")
   else:
      print("this expense not avalible. ")

def delet_expense():
   v= input("you can delet expense:- ")
     
   if v in d :
      d.pop(v)
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


  
        ##### bank account managmnet system #####

      

SBI = 100000

def diposit_money():
     v= input("enter amount:-").isdigit()
     v=int(v)
     print("money added ")
     print(SBI+v)
 

def withdrawal_money():
     v= input("enter withdrawal amount:-").isdigit()
     v=int(v)
     if v < SBI:
         print("withdrawal sucessfully.",SBI-v)
     else :
          print("cheak bank balance..",SBI)


def display_money():
     print(SBI)
 
while True:
    print("==== bank account Management System ====")
    print("1. diposit money.")
    print("2.  withdrawal money.")
    print("3. show bank balance.")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        diposit_money()
    elif choice == "2":
        withdrawal_money()
    elif choice == "3":
        display_money()  
    elif choice == "4":
        break
    else:
      print("Invalid choice. Please try again.")



      ##### inventry managment system #####




d = {
    "pen":85,
    "books":55,
    "notepaed":40
}

def add_inventry():
    v= input("enter inventry name:-")
    m= input("enter stock:-")
    d[v]=m
    print(d)

def display_inventry():
    print(d)
 
def search_invrntry():
    v=input("find item :-")
    if v in d.keys():
        print("allready avalible.")
    else:
        print("not found this inventry.")
    print(d)

def update_inventry():
    v=input("enter inventry:-") 
    m=input("enter value:-") 
     
    d[v]=m
    print(d)

def delet_invantry():
    v= input("inventry delet:-")
    if v in d :
        d.pop(v)
    else:
        print("not found.")
    print(d)



while True :
    print('=====inventry managment system=====')
    print("1,add invantry.")
    print("2,show invantry.")
    print("3,search inventry.")
    print("4,update inventry.")
    print("5,delet inventry.")
    print("6,exit...")

    choice = int(input("choice 1 to 6."))

    if choice == 1 :
        add_inventry()
    elif choice == 2 :
        display_inventry()
    elif choice == 3 :
        search_invrntry()
    elif choice == 4 :
        update_inventry()
    elif choice == 5 :
        delet_invantry()
    elif choice == 6 :
        break
    else:
        print("invalide choice...")



