import matplotlib.pyplot as mtp
 
class Student:

    def __init__(self, name, roll_number, city, math, science, english):

        self.name = name
        self.roll_number = roll_number
        self.city = city
        self.math = math
        self.science = science
        self.english = english


    def total(self):
        return self.math + self.science + self.english


    def percentage(self):
      return  self.total() / 3


    def grade(self):

        per = self.percentage()

        if per >= 90:
            print("A+")

        elif per >= 80:
            print("A")

        elif per  >= 70:
            print("B")

        elif per  >= 60:
            print("c")

        elif per >= 50:
            print("D")
        elif per >= 35:
            print("E")
        else:
             "Fail"
     
    def result(self):

        if self.math >= 35 and self.science >= 35 and self.english >= 35:
             return "You Are Pass."

        else:
            return "Fail.."


  
    def show(self):

        print("----------------------")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("City:", self.city)
        print("Math:", self.math)
        print("Science:", self.science)
        print("English:", self.english)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())
        print("Result:", self.result())
 

class result:

    def __init__(self):
        self.students = []

    def find_student(self, roll_number):

        for student in self.students:

            if student.roll_number == roll_number:

                return student

        return None
  
    def create_student(self):
       
        name = input("Student name:- ")
        if name.replace(" ", "",1).isalpha():

            roll_number = input("Roll number:- ")
            if roll_number.isdigit():

                if self.find_student(roll_number) == None:

                    city = input("City:- ")
                    if city.replace(" ", "").isalpha():

                        math = input("Math marks:- ")
                        science = input("Science marks:- ")
                        english = input("English marks:- ")

                        if math.isdigit():
                            if science.isdigit():
                                if english.isdigit():

                                    math = int(math)
                                    science = int(science)
                                    english = int(english)

                                    if math <= 100 and science <= 100 and english <= 100:

                                        student = Student(
                                            name,
                                            roll_number,
                                            city,
                                            math,
                                            science,
                                            english
                                        )

                                        self.students.append(student)

                                        print("Student Added Successfully")

                                    else:
                                        print("Marks cannot be greater than 100")

                                else:
                                    print("Invalid English Marks")

                            else:
                                print("Invalid Science Marks")
                        else:
                            print("Invalid Math Marks")
                    else:
                        print("Invalid City")
                else:
                    print("Roll Number Already Exists")
            else:
                print("Invalid Roll Number")
        else:
            print("Invalid Name")

    def show_all(self):

        if self.students:
            print("No Student Data")

            for student in self.students:
                student.show()
        else:
            print("Not data'")


    def search(self):

        roll_number = input("Enter roll number:- ")
        a= self.find_student(roll_number)


        if a:
            a.show()

        else:
            print("Student Not Found")

    def update(self):

        roll_number = input("Enter roll number:- ")
        a = self.find_student(roll_number)

        if a in self.student:

            while True:

                print("----------------------")
                print("1. Update Name")
                print("2. Update City")
                print("3. Update Math Marks")
                print("4. Update Science Marks")
                print("5. Update English Marks")
                print("6. Done")

                choice = input("Enter choice:- ")


                if choice == "1":
                    name = input("New name:- ")

                    if name.replace(" ", "").isalpha():
                        a.name = name
                        print("Name Updated")
                    else:
                        print("Invalid Name")

                elif choice == "2":
                    city = input("New city:- ")

                    if city.replace(" ", "").isalpha():
                        a.city = city
                        print("City Updated")
                    else:
                        print("Invalid City")

                elif choice == "3":
                    marks = input("New Math marks:- ")

                    if marks.isdigit():
                        if int(marks) <= 100:
                            a.math = int(marks)
                            print("Math Marks Updated")
                        else:
                            print("Marks cannot be greater than 100")
                    else:
                        print("Invalid Marks")


                elif choice == "4":
                    marks = input("New Science marks:- ")

                    if marks.isdigit():
                        if int(marks) <= 100:
                            a.science = int(marks)
                            print("Science Marks Updated")
                        else:
                            print("Marks cannot be greater than 100")
                    else:
                        print("Invalid Marks")


                elif choice == "5":
                    marks = input("New English marks:- ")

                    if marks.isdigit():
                        if int(marks) <= 100:
                            a.english = int(marks)
                            print("English Marks Updated")
                        else:
                            print("Marks cannot be greater than 100")
                    else:
                        print("Invalid Marks")


                elif choice == "6":
                    print("Update Complete")
                    break

                else:
                    print("Wrong Choice")
        else:
            print("Student Not Found")


    def delete(self):

        roll_number = input("Enter roll number:- ")
        student = self.find_student(roll_number)

        if student:
            self.students.remove(student)
            print("Student Deleted")
        else:
            print("Student Not Found")
 
    def result_chart(self):

        if self.students == 0:
            print("No Student Data")
     
        names = []
        percentages = []

        for student in self.students:

            names.append(student.name)
            percentages.append(student.percentage())


        mtp.bar(names, percentages)

        mtp.title("Student Percentage")
        mtp.xlabel("Students")
        mtp.ylabel("Percentage")
        mtp.show()

    def results(self):
        roll = input("Enter roll number:- ")
        a = self.find_student(roll)

        if a:
            print("Percentage:", round(a.percentage(), 2))
            print("Grade:", a.grade())
            print("Result:", a.result())
        else:
            print("Student Not Found")

    def marks(self):
        roll = input("Enter roll number:- ")
        a = self.find_student(roll)

        if a:
            print("Math:", a.math)
            print("Science:", a.science)
            print("English:", a.english)
            print("Total:", a.total())

        else:
            print("Student Not Found")
while True:

    print("========= STUDENT RESULT ANALYSIS ==========")

    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Result Analysis")
    print("7. Show Top Student")
    print("8. Percentage Chart")
    print("9. Subject Average Chart")
    print("10. Show Student Result")
    print("11. Show Student Marks")
    print("12. Exit")

    choice = input("Enter your choice:- ")

    if choice == "1":
        result.create_student("self")

    elif choice == "2":
        result.show_all()

    elif choice == "3":
        result.search()

    elif choice == "4":
        result.update()

    elif choice == "5":
        result.delete()

    elif choice == "6":
        result.result_analysis()

    elif choice == "7":
        result.top_student()

    elif choice == "8":
        result.result_chart()

    elif choice == "9":
        result.subject_chart()

    elif choice == "10":
        result.results()

    elif choice == "11":
        result.marks()

    elif choice == "12":
        print("Thank you")
        break

    else:
        print("Wrong Choice")