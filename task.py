students = []

for i in range(2):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    marks = list(map(int, input("Enter 3 marks: ").split()))

    total = sum(marks)
    percentage = total / 3

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    students.append({
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    })

# Table print
print("\n")
print("-" * 60)
print(f"{'Name':<15}{'Total':<10}{'Percentage':<15}{'Grade':<10}")
print("-" * 60)

for s in students:
    print(f"{s['name']:<15}{s['total']:<10}{s['percentage']:<15.2f}{s['grade']:<10}")

# Highest marks student
highest = students[0]
lowest = students[0]

for s in students:
    if s["total"] > highest["total"]:
        highest = s

    if s["total"] < lowest["total"]:
        lowest = s

print("\nHighest Marks Student:")
print(highest["name"], "-", highest["total"])

print("\nLowest Marks Student:")
print(lowest["name"], "-", lowest["total"])

 
 