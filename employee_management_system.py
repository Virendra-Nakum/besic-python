d= {
    "raj": 1512,
    "rahul":1212,
    "virendra":1412,
    "dev":1215
}

def add_employee():
    employee= input("enter employee name:-")
    ID= input("employee ID:-")
    if employee.isalpha() and ID.isalpha() :
        d[employee]=ID
    else: 
        print("try only alphabet.")
    print(d)

def dispaly_employee():
    print(d)
 
def search_employee():
    employee= input("find employee:-")
    if employee.isalpha() :
        if employee in d.keys() :
            print("yes , employee are avalible here..")
        else:
            print("not found , tihs employee.")
    else:
        print("try only alphabet.")
 
def update_emploee():
    employee= input("enter update name:-") 
    ID= input("enter empolyees ID:-") 
    if employee.isalpha() and ID.isdigit():
        employee=str(employee) 
        ID=int(ID)
        d[employee]=ID
    else:
     print("try again.")
    print(d)
 

def delet_employee():
    employee=input("delet an empolyee:-")

    if employee in d  :
       d.pop(employee)
    else:
        print("employee not found...")
    
 
 
while True:
    print("====== employee Management System ======")
    print("1. Add employee")
    print("2. View employee")
    print("3. Search employee")
    print("4. update employee")
    print("5. delet employee.")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        dispaly_employee()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_emploee()
    elif choice == "5":
        delet_employee()
    elif choice == "6":
        break
    else:
      print("Invalid choice. Please try again.")

  