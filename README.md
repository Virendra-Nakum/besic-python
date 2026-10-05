# Student Performance Management System

A Python-based console application for managing student records, marks, attendance, grades, and class performance.

## Features

- Login and account management
- Create account
- Change password
- Add student records
- View student records
- Search student by ID
- Update student information
- Remove student records
- Marks analysis
- Percentage calculation
- Grade and Pass/Fail analysis
- Attendance analysis
- Short attendance detection
- Class statistics
- Top performers
- Save student data using JSON
- Load saved data automatically
- Input validation and exception handling

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON
- Lambda Functions
- Filter Function
- List and Dictionary
- Exception Handling
- File Handling

## OOP Concepts Used

### Class

The project uses multiple classes:

- `Student`
- `StudentManager`
- `StudentAnalytics`

### Encapsulation

Student data and related methods are grouped inside classes.

### Inheritance

`StudentAnalytics` inherits from `StudentManager`.

```python
class StudentAnalytics(StudentManager):
Polymorphism / Method Overriding

StudentAnalytics overrides the search_student() method.

Static Method

valid_marks() is implemented using @staticmethod.

Class Method

from_dict() is implemented using @classmethod.

Property

The percentage value is calculated using @property.

Project Structure
Student-Performance-Management-System/
│
├── main.py
├── File.json
└── README.md
How to Run
Step 1: Open the project in VS Code

Open the project folder in Visual Studio Code.

Step 2: Open Terminal

In VS Code:

Terminal → New Terminal
Step 3: Run the program
python main.py
Main Menu
1. Login
2. Add Student
3. View Student
4. Search Student
5. Update Student
6. Marks Analysis
7. Grade / Pass-Fail
8. Attendance
9. Class Statistics
10. Top Performers
11. Save
12. Exit
Student Information

The system stores:

Student ID
Student Name
Student Age
Course
Subjects
Marks
Attendance
Percentage
Marks Analysis

The system calculates:

Total Marks
Percentage
Average Marks
Highest Marks
Lowest Marks
Failed Subject Marks
Grade System
Percentage	Grade
90+	A+
80–89	A
70–79	B+
60–69	B
50–59	C
40–49	D
Below 40	E

A student fails if any subject has marks below 33.

Attendance

Students having attendance below 70% are displayed as having short attendance.

JSON Data Storage

Student records are saved in:

File.json

The program uses Python's json module to save and load student data.

Error Handling

The application handles invalid user input using try-except.

For example:

try:
    student_id = int(input("Enter Student ID:- "))
except ValueError:
    print("Enter a valid Student ID.")

This prevents the program from crashing because of invalid input.

Learning Concepts

This project helped practice:

Python Functions
Classes and Objects
Constructors
self
Inheritance
Method Overriding
Encapsulation
Static Methods
Class Methods
Properties
Lambda Functions
filter()
Lists
Loops
Exception Handling
File Handling
JSON
CRUD Operations
Future Improvements

Possible future improvements:

Database integration
GUI application
Web application
User authentication with secure password storage
Export reports to Excel/PDF
Student performance charts
Admin dashboard
Author

Virendra Nakum

Python Developer | Data Science & AI/ML Learner

Jamnagar, Gujarat, India

 
```
Student Performance Management System
│
├── main.py
├── File.json
└── README.md

```
