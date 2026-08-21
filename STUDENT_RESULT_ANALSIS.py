import numpy as np
import matplotlib.pyplot as mtp 

class Student :
    def __init__(self,id,name,marks) :
        self.id = id
        self.name = name
        self.__marks = marks

    def get_marks(self):
       return self.__marks  

    def Display_student(self):
        a = np.array(self.__marks)
        total =  a.sum()
        per = total /len(a)

        print("Student ID:",self.id)
        print("Student Name:",self.name)
        print("Student Total Mark:",total)
        print("Student Persatnge",round(per,2),"%")

class S :
    def __init__(self):
        self.student = [
            Student(1,"villan",[89,90,79]),
            Student(4,"villan",[83,50,69]),
            Student(2,"villan",[87,95,49])
                        ]
  
    def add_student(self):
        print("------------ ADD STUDENT -----------")
 
        while True :
            try:
                Id = int(input("Enter student ID:-"))
                for std in self.student :
                    if std == Id :
                        print("Already Exists.")
                        break
                else:
                    break
            except:
                print("Enter Valid Data.")

        while True:
            try :
                name = input("Enter Student Name:-")
                if len(name) >=2 and len(name)<=50 and name.replace(" ","",50).isalpha():
                    print("Name ADD .")
                    break
            except:
                print("Enter Valid Name.")

        marks = []
        subjects = ["Python","java","C++"]
        for subject in subjects :
            while True :
                try:
                    mark = int(input(f"Enter Mark {subject}:-"))
                    if mark >=0 and mark <=100 :
                        m = marks.append(mark)
                        break
                    else:
                        print("Mark must been Grater 100 ")
  
                except:
                    print("Enter Valid Mark.")

            New_student= Student[id,name,marks]
            self.student.append(New_student)

    def show_student(self):
        print("------------ SHOW ALL STUDENT --------------")
        if len(self.student) !=0 :
            for std in self.student :
                 std.Display_student()
        else:
            print("data not found.")

    def search_student(self):
        print("----------- SEARCH STUDENT ---------------")
        if len(self.student) !=0 :
            try:

                id = int(input("Enter student ID :-"))
                for std in self.student :
                    if std.id == id :
                        std.Display_student() 
                        break
                else:
                    print("Student not found.")
            except:
                print("Enter valid input.")
        else:
            print("data not found.")



    def update_student(self):
        print("----------------UPDATE STUDENT DETIELS---------------")

        
        try :
            id = int(input("enter student id:-"))
            for std in self.student :
                if std.id == id :

                    while True :
                        print("1.UPDATE NAME.")
                        print("2.UPDATE MARKS.")
                        print("3.EXIT.....")

                        try :
                            choice = int(input("enter choice:-"))

                            if choice == 1 :
                                name = input("Enter Student Name:-")
                                if len(name) >=2 and len(name)<=50 and name.replace(" ","",50).isalpha():
                                    print("Updated ")
 
                                else:
                                    print("try again.")

                            elif choice == 2 :
                                    marks = ["Python", "Java"," C++"]

                                    while True :
                                        print("1. UPDATE PYTHON MARK")
                                        print("2. UPDATE JAVA MARK")
                                        print("3. UPDATE C++ MARK")
                                        print("4. EXIT...")

                                        try:
                                            update_choice = int(input("Enter Your Choice:- "))

                                            if update_choice >= 1 and update_choice <= 3:

                                                mark = int(input("Enter New Mark:- "))

                                                if mark >= 0 and mark <= 100:
                                        

                                                    if update_choice == 1:
                                                        marks[0] = mark
                                                        print("Python Mark Updated.")

                                                    elif update_choice == 2:
                                                        marks[1] = mark
                                                        print("Java Mark Updated.")

                                                    elif update_choice == 3:
                                                        marks[2] = mark
                                                        print("C++ Mark Updated.")

                                                    elif update_choice == 4 :
                                                        print("Exits....")
                                                        break

                                                else:
                                                    print("Mark Must Be Between 0 and 100.")
                                            else:
                                                print("Invalide choice.")
                                                break
 
                                        except:
                                            print("Enter Number Only.")
                            elif choice == 3 :
                                print("Exit..")
                                break

                            else :
                                print("Invalide choice.")
                      
                        except:
                            print("Invalide input.")
                    break
            else:
                print("Student Not Found .")
        
        except:
            print("Enter valide ditels.")

    def remove_student(self):
        print("---------- REMOVE STUDENT ----------")
        if len(self.student) !=0 :
            try:
                std_id = int(input("Enter Student ID:-"))
                for std in self.student :
                    if std.id == std_id :
                        self.student.remove(std)
                        print("Student Remove Succ.....")
                        break
                else:
                    print("Student Not Found.")
            except :
                print("Try Only Numbers.")
        else:
            print("Data Not Found.")

    def Graph_Student(self):
        print("--------- STUDENT PERFOMENCE ---------")
        try:

            id = int(input("Enter Student ID:-"))

            for std in self.student :
                if std.id == id :
            
                    while True :

                        print("1. BAR CHART.")
                        print("2. PIE CHART.")
                        print("3. LINE GRAPH CHART.")
                        print("4. EXIT.")
    
                        choise = input("Enter choise (1to4):-")
                        if choise == "1" :
    
                            subject = ["Python","Java","C++"]
                            marks =  std.get_marks() 
                            mtp.bar( subject,marks   )
                            mtp.xlabel("Subject")
                            mtp.ylabel("Marks")
                            mtp.title("Student Marks")
                            mtp.ylim(0, 100)
                            mtp.legend()
                            mtp.show()

 
                        elif choise =="2" :
                            subject = ["Python","Java","C++"]
                            marks = std.get_marks()
                            mtp.pie(marks, labels=subject, autopct='%1.1f%%')
                            mtp.title("Student Marks Distribution")
                            mtp.show()


                        elif choise == "3":
                            subject = ["Python","Java","C++"]
                            marks = std.get_marks()
                            mtp.plot(subject, marks, marker='o')
                            mtp.title("Progress Tracker")
                            mtp.show()

  
                        elif choise == "4" :
                            print("Thank You For Useing Graph .")
                            break

                        else:
                            print("Enter Valid Choise..")
                break

            else:
                print("Student Not Found.")

        except:
            print("Enter Valid Id..")

a = S()

while True:

    print("1. Update Student")
    print("2. Add Student")
    print("3. Show Student")
    print("4. Search Student")
    print("5. Remove Student")
    print("6. Graph Student")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        a.update_student()

    elif choice == "2":
        a.add_student()

    elif choice == "3":
        a.show_student()

    elif choice == "4":
        a.search_student()

    elif choice == "5":
        a.remove_student()

    elif choice == "6":
        a.Graph_Student()

    elif choice == "7":
        print("Thank You For Use Student Result Analisis Project...")
        break

    else:
        print("Invalid Choice!")