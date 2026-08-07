# import matplotlib.pyplot as plt
# import numpy as np


# # ==========================
# # Student Class
# # ===========================

# class Student:

#     def __init__(self, roll, name, english, maths, science):
#         self.roll = roll
#         self.name = name
#         self.english = english
#         self.maths = maths
#         self.science = science
    
#     def total_marks(self):
#         a = self.english + self.maths + self.science

#     def percentage(self):
#         b= self.total_marks() / 3

#     def grade(self):

#         per = self.percentage()

#         if per >= 90:
#             return "A+"

#         elif per >= 80:
#             return "A"

#         elif per >= 70:
#             return "B"

#         elif per >= 60:
#             return "C"

#         elif per >= 50:
#             return "D"

#         else:
#             return "Fail"

# # ==========================
# # List of Objects
# # ==========================

# students = []

# # ==========================
# # Input Validation
# # ==========================

# def get_marks(subject):

#     while True:

#         try:
#             marks = int(input(f"Enter {subject} Marks : "))

#             if 0 <= marks <= 100:
#                 return marks

#             else:
#                 print("Marks must be between 0 and 100")

#         except:
#             print("Invalid Input")

# # ==========================
# # Add Student
# # ==========================

# def add_student():

#     try:

#         roll = int(input("Enter Roll Number : "))

#         for s in students:
#             if s.roll == roll:
#                 print("Roll Number Already Exists")
#                 return

#         name = input("Enter Name : ")

#         english = get_marks("English")
#         maths = get_marks("Maths")
#         science = get_marks("Science")

#         student = Student(
#             roll,
#             name,
#             english,
#             maths,
#             science
#         )

#         students.append(student)

#         print("Student Added Successfully")

#     except:
#         print("Error")

# # ==========================
# # View Students
# # ==========================

# def view_students():

#     if len(students) == 0:
#         print("No Students Found")
#         return

#     print("-" * 80)

#     print(
#         "Roll\tName\tEnglish\tMaths\tScience\tTotal\tPer\tGrade"
#     )

#     print("-" * 80)

#     for s in students:

#         print(
#             f"{s.roll}\t{s.name}\t{s.english}\t{s.maths}\t{s.science}\t{s.total_marks()}\t{s.percentage():.2f}\t{s.grade()}"
#         )

# # ==========================
# # Search Student
# # ==========================

# def search_student():

#     roll = int(input("Enter Roll Number : "))

#     found = False

#     for s in students:

#         if s.roll == roll:

#             print("\nStudent Found")

#             print("Roll :", s.roll)
#             print("Name :", s.name)
#             print("English :", s.english)
#             print("Maths :", s.maths)
#             print("Science :", s.science)
#             print("Total :", s.total_marks())
#             print("Percentage :", round(s.percentage(), 2))
#             print("Grade :", s.grade())

#             found = True

#     if found == False:
#         print("Student Not Found")

# # ==========================
# # Update Student
# # ==========================

# def update_student():

#     roll = int(input("Enter Roll Number : "))

#     for s in students:

#         if s.roll == roll:

#             print("1. Update Name")
#             print("2. Update Marks")

#             ch = int(input("Choice : "))

#             if ch == 1:

#                 new_name = input("Enter New Name : ")

#                 s.name = new_name

#                 print("Name Updated")

#             elif ch == 2:

#                 s.english = get_marks("English")
#                 s.maths = get_marks("Maths")
#                 s.science = get_marks("Science")

#                 print("Marks Updated")

#             return

#     print("Student Not Found")

# # ==========================
# # Delete Student
# # ==========================

# def delete_student():

#     roll = int(input("Enter Roll Number : "))

#     for s in students:

#         if s.roll == roll:

#             students.remove(s)

#             print("Student Deleted")

#             return

#     print("Student Not Found")

# # ==========================
# # Statistics
# # ==========================

# def statistics():

#     if len(students) == 0:
#         print("No Data")
#         return

#     percentages = []

#     for s in students:
#         percentages.append(s.percentage())

#     arr = np.array(percentages)

#     print("\nStatistics")

#     print("Average :", np.mean(arr))
#     print("Highest :", np.max(arr))
#     print("Lowest :", np.min(arr))

# # ==========================
# # Topper
# # ==========================

# def topper():

#     if len(students) == 0:
#         print("No Data")
#         return

#     top = students[0]

#     for s in students:

#         if s.percentage() > top.percentage():
#             top = s

#     print("\nTopper")

#     print("Name :", top.name)
#     print("Percentage :", top.percentage())

# # ==========================
# # Result Summary
# # ==========================

# def result_summary():

#     pass_count = 0
#     fail_count = 0

#     for s in students:

#         if s.grade() == "Fail":
#             fail_count += 1
#         else:
#             pass_count += 1

#     print("Pass :", pass_count)
#     print("Fail :", fail_count)
# # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # ==========================
# # Bar Chart
# # ==========================

# def bar_chart():

#     if len(students) == 0:
#         print("No Data Available")
#         return

#     names = []
#     percentages = []

#     for s in students:
#         names.append(s.name)
#         percentages.append(s.percentage())

#     plt.figure(figsize=(8,5))
#     plt.bar(names, percentages)
#     plt.title("Student Percentage")
#     plt.xlabel("Students")
#     plt.ylabel("Percentage")
#     plt.ylim(0,100)
#     plt.show()

# # ==========================
# # Pie Chart
# # ==========================

# def pie_chart():

#     if len(students) == 0:
#         print("No Data Available")
#         return

#     pass_count = 0
#     fail_count = 0

#     for s in students:
#         if s.grade() == "Fail":
#             fail_count += 1
#         else:
#             pass_count += 1

#     plt.figure(figsize=(6,6))
#     plt.pie(
#         [pass_count, fail_count],
#         labels=["Pass","Fail"],
#         autopct="%1.1f%%"
#     )
#     plt.title("Pass / Fail Analysis")
#     plt.show()

# # ==========================
# # Subject Average
# # ==========================

# def subject_average():

#     if len(students) == 0:
#         print("No Data")
#         return

#     eng = []
#     maths = []
#     sci = []

#     for s in students:
#         eng.append(s.english)
#         maths.append(s.maths)
#         sci.append(s.science)

#     print("\nSubject Average")
#     print("English :", np.mean(eng))
#     print("Maths :", np.mean(maths))
#     print("Science :", np.mean(sci))

# # ==========================
# # Save Data
# # ==========================

# def save_data():

#     file = open("students.txt","w")

#     for s in students:

#         file.write(
#             f"{s.roll},{s.name},{s.english},{s.maths},{s.science}\n"
#         )

#     file.close()

#     print("Data Saved Successfully")

# # ==========================
# # Load Data
# # ==========================

# def load_data():

#     try:

#         file = open("students.txt","r")

#         students.clear()

#         for line in file:

#             data = line.strip().split(",")

#             student = Student(
#                 int(data[0]),
#                 data[1],
#                 int(data[2]),
#                 int(data[3]),
#                 int(data[4])
#             )

#             students.append(student)

#         file.close()

#         print("Data Loaded Successfully")

#     except FileNotFoundError:
#         print("No Saved File Found")

# # ==========================
# # Sample Data
# # ==========================

# def sample_data():

#     students.clear()

#     students.append(Student(101,"Rahul",80,75,90))
#     students.append(Student(102,"Amit",60,70,68))
#     students.append(Student(103,"Riya",95,92,98))
#     students.append(Student(104,"Priya",45,52,48))
#     students.append(Student(105,"Jay",88,91,85))

#     print("Sample Data Added")

# # ==========================
# # Menu
# # ==========================

# def menu():

#     while True:

#         print("\n")
#         print("="*50)
#         print(" STUDENT RESULT ANALYSIS SYSTEM ")
#         print("="*50)

#         print("1. Add Student")
#         print("2. View Students")
#         print("3. Search Student")
#         print("4. Update Student")
#         print("5. Delete Student")
#         print("6. Statistics")
#         print("7. Topper")
#         print("8. Result Summary")
#         print("9. Subject Average")
#         print("10. Bar Chart")
#         print("11. Pie Chart")
#         print("12. Save Data")
#         print("13. Load Data")
#         print("14. Add Sample Data")
#         print("15. Exit")

#         try:

#             choice = int(input("Enter Choice : "))

#             if choice == 1:
#                 add_student()

#             elif choice == 2:
#                 view_students()

#             elif choice == 3:
#                 search_student()

#             elif choice == 4:
#                 update_student()

#             elif choice == 5:
#                 delete_student()

#             elif choice == 6:
#                 statistics()

#             elif choice == 7:
#                 topper()

#             elif choice == 8:
#                 result_summary()

#             elif choice == 9:
#                 subject_average()

#             elif choice == 10:
#                 bar_chart()

#             elif choice == 11:
#                 pie_chart()

#             elif choice == 12:
#                 save_data()

#             elif choice == 13:
#                 load_data()

#             elif choice == 14:
#                 sample_data()

#             elif choice == 15:

#                 print("Thank You")
#                 break

#             else:

#                 print("Invalid Choice")

#         except ValueError:

#             print("Enter Numbers Only")

# # ==========================
# # Main
# # ==========================

# if __name__ == "__main__":

#     menu()


