l={
    "ram":67,
    "syam":66,
    "hanuman":90
}
def display():
    print(l)
 

def add_():
    name= input("What's your superhero name? 😎: ")
    marks=input("📚 How many marks did you score? 😄: ")

    if name.isalpha() and marks.isdigit():
        l[name]=marks
        print(l)
        print("added sucessfully.")
    else:
        print("data not found")


def update_():
    name = input("update too specific name,marks:")
    marks = input("📚 change the marks  your score? 😄:")

    if name.isalpha() and marks.isdigit():
        marks=int(marks)
        l[name]=marks
        print(l)
        print("update your marks.")
    else:
        print("name,marks not found.")

def delet_():

    v=input("enter name you are remove.")
    if v in l:
            del l[v]
            print("Deleted")
            print(l)
    else:
            print("Not found")
            
                    


while True:
     print("1. you seen dictnory . ")
     print("2. you added name,marks. ")
     print("3. you update name,marks. ")
     print("4. you delete name,marks. ")
     print("5. exit... ")

     choise = input("choise between 1 to 5. ")

     if choise == "1":
        display()
     elif choise == "2":
        add_()
        
     elif choise == "3":
         update_()
     elif choise == "4":
        delet_()
        
     elif choise == "5" :
        print("exit...")
        break