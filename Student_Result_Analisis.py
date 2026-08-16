import numpy as np
import matplotlib.pyplot as mpl
std = [

    {
        "id": 1,
        "name": "Virendra",
        "math": 85,
        "physics": 78,
        "chemistry": 92,
        "science": 88
    },

    {
        "id": 2,
        "name": "Rahul",
        "math": 72,
        "physics": 80,
        "chemistry": 75,
        "science": 79
    },

    {
        "id": 3,
        "name": "Neha",
        "math": 99,
        "physics": 88,
        "chemistry": 95,
        "science": 90
    },

    {
        "id": 4,
        "name": "Amit",
        "math": 65,
        "physics": 70,
        "chemistry": 68,
        "science": 72
    },

    {
        "id": 5,
        "name": "Priya",
        "math": 45,
        "physics": 52,
        "chemistry": 48,
        "science": 55
    },

    {
        "id": 6,
        "name": "Karan",
        "math": 88,
        "physics": 90,
        "chemistry": 84,
        "science": 86
    },

    {
        "id": 7,
        "name": "Pooja",
        "math": 76,
        "physics": 69,
        "chemistry": 81,
        "science": 74
    },

    {
        "id": 8,
        "name": "Jay",
        "math": 55,
        "physics": 61,
        "chemistry": 58,
        "science": 63
    },

    {
        "id": 9,
        "name": "Riya",
        "math": 96,
        "physics": 94,
        "chemistry": 89,
        "science": 97
    },

    {
        "id": 10,
        "name": "Arjun",
        "math": 38,
        "physics": 42,
        "chemistry": 35,
        "science": 40
    }

]
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
    
    def display(self):

        arr =np.array([])

        total = np.sum(arr)
        average = np.mean(arr)
        per= (total/len()*100)*100

        print("-----------------------------")
        print("Student ID   :", self.student_id)
        print("Student Name :", self.name)
        print("Total Marks  :", total)
        print("Average      :", average)
        print("Percentage   :",round(per,2), "%")

        if per >= 90:
            grade = "A+"

        elif per >= 80:
            grade = "A"

        elif per >= 70:
            grade = "B"

        elif per >= 60:
            grade = "C"

        elif per >= 50:
            grade = "D"

        elif per >= 35:
            grade = "E"

        else:
            grade = "Fail"


        print("Grade:", grade)
        print("-----------------------------")

 

def add_student():
 
    print("------ ADD STUDENT ------")

    while True:

        try:
            student_id = int(input("Enter Student ID:- "))
            
            for student in std:
                if student["id"] == student_id:
                    print("Student Already Exists.")
                    break
            
            else:
                print("Student ID Available.")
                break
        except:
            print("You Type whatever? Just Try Only Number.")
 
    
    while True:

        name = input("Enter Student Name: ").strip()

        if name.isalpha()and name.replace(" ","",2):
            print(name)
            break
        else:
            print("You Type whatever ? Just Try Only Alphabet.")
            
    print("Enter marks out of 100")

    while True:
        try:
        
            Math= int(input("Mathematics Marks:-"))
            if Math >=1 and Math <=100 :
                print(Math)
                break
            else:
                print("I Think Mark Not UP 100. Right ? ")
        except:
            print("Use only Number.")
 
    while True:
        try :
            phy = int(input("Physic mark:-"))
            if phy >=0 and phy <=100 :
                print(phy)
                break
            else: 
                print("I Think Mark Not UP 100. Right ? ")
        except:
            print("You Type whatever ? Just Try Only Number.")
            
  
    while True:
        try:
            chr = int(input("Chemistry Marks: "))

            if chr >=0 and chr <=100 :
                print(chr)
                break
            else:
                print("I Think Mark Not UP 100. Right ? ")
        except:
            print("You Type whatever ? Just Try Only Number.")


    while True:
        try:
            science = int(input("Science Marks: "))
            if science >=0 and science <=100 :
                print(science)
                break
            else:
                print("I Think Mark Not UP 100. Right ?")
        except:
            print("You Type whatever ? Just Try Only Number.")
        

    Student = {               
        "id": student_id,
        "name": name,
        "math": Math,
        "physics": phy,
        "chemistry": chr,
        "science": science
    }

    std.append(Student)
    print("Student added successfully!")


def view_students():

    print("------ ALL STUDENTS ------")
    try :

        v = int(input("Enter Your ID:- "))
        for student in std :

            if student["id"] == v :

                print("----------------------")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Math:", student["math"])
                print("Physics:", student["physics"])
                print("Chemistry:", student["chemistry"])
                print("Science:", student["science"])
                break
        else:
            print("Student Not Found")
    except:
        print("You Type whatever ? Just Try Only Number.")


 

def search_student():

    print("------ SEARCH STUDENT ------")
    try:

        v = int(input("Enter Your ID:- "))
    
        for student in std:

            if student["id"] == v:

                print("----------------------")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Math:", student["math"])
                print("Physics:", student["physics"])
                print("Chemistry:", student["chemistry"])
                print("Science:", student["science"])
                break

        else:
            print("Student Not Found")
    except:
        print("You Type whatever ? Just Try Only Number.")
        
 
 
def update_student():

    try:

        id = int(input("Enter Your ID:- "))

        for student in std :
            if student["id"] == id  :
                print("Student Found.")
        
                while True:

                    print("----------------------")
                    print("1. Update Name")
                    print("2. Update Your ID")
                    print("3. Update Marks")
                    print("4. Exit")

                    choice = int(input("Enter Choice (1to4):- "))

                    if choice == 1:
                        name = input("New Name:- ")
                        std["name"] = name
                        print("Name Updated")


                    elif choice == 2:
                        roll = int(input("New Roll Number:- "))
                        std["roll"] = roll
                        print("Roll Number Updated")

                    elif choice == 3:
                        m= int(input("Math:- "))
                        p = int(input("Physics:- "))
                        c= int(input("Chemistry:- "))
                        s= int(input("Science:- "))

                        if m<= 100 and p <= 100 and c<= 100 and s <= 100:

                            std["math"] = m
                            std["physics"] = p
                            std["chemistry"] = c
                            std["science"] = s
                            print("Marks Updated")

                        else:
                            print("I Think Mark Not UP 100. Right ? ")

                    elif choice == 4:
                        print("Update Complete")
                        break
        else:
            print("Student Not Found.")
 
    except :
        print("You Type whatever ? Just Try Only Number.")

def delete_student():

    print("------ DELETE STUDENT -----")

    try:
        id = int(input("Enter Your ID:-"))
        for student in std :
            if student["id"] == id :
                print("Student In This Class ")
                std.clear()
                print("Student Deleted.")
        else:
            print("Student Not Found.")
    except:
            print("You Type whatever ? Just Try Only Number.")
        

def numpy_analysis():

    print("--------- RESULT ANALYSIS --------")
    try:
        id = int(input("Enter Student ID:- "))
        
        for student in std:
            if student["id"] == id:
                marks = np.array([
                    student["math"],
                    student["physics"],
                    student["chemistry"],
                    student["science"]])

                print("Name    :", student["name"])
                print("Marks   :", marks)
                print("Total   :", np.sum(marks))
                print("Average :", np.mean(marks))
                print("Highest :", np.max(marks))
                print("Lawest  :", np.min(marks))
                break
        else:
            print("Student not found.")
    except:
        print("You Type whatever ? Just Try Only Number.")

    
def show_graph():
    print("--------- STUDENT PERFORMANCE GRAPH ---------")
    try: 
        id = int(input("Enter Student ID:-"))
    
        for student in std :
            if student["id"] == id :
                subject = ["Math","Physics","Chemistry","Science"]
                
                marks =[ student["math"],
                student["physics"],
                student["chemistry"],
                student["science"],]
 
                mpl.bar(subject,marks,label= student["name"])
                mpl.title("Student Performance " )
                mpl.xlabel("Subjects")
                mpl.ylabel("Marks") 
                mpl.ylim(0, 100)
                mpl.legend()
                mpl.show()
        else:
            print("Student Not Found.")
    except:
        print("You Type whatever ? Just Try Only Number.")


while True:

    print("------------------------------")
    print("      STUDENT MANAGEMENT")
    print("------------------------------")


    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Result Analysis")
    print("7. Show Graph")
    print("8. Exit")


    choice = input("Enter your choice: ")


    if choice == "1":
        add_student()


    elif choice == "2":
        view_students()


    elif choice == "3":
        search_student()


    elif choice == "4":
        update_student()


    elif choice == "5":
        delete_student()


    elif choice == "6":
        numpy_analysis()


    elif choice == "7":
        show_graph()


    elif choice == "8":
        print("Thank You For Using Student Result Analsis System.")
        print("Developed By Mr. Virendra.")
        break

    else:
        print("Try only 1to8")
