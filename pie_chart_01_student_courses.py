import matplotlib.pyplot as mtp
import numpy as np

students = np.array([40, 25, 20, 15])
courses = ["Python", "AI/ML", "Data Science", "Web Dev"]
 
mtp.figure(figsize=(6,6), facecolor="lightgray")

# Graph Background
mtp.gca().set_facecolor("lightyellow")

mtp.pie(
    students,
    labels=courses,
    autopct="%.2f%%",
    colors=["red", "blue", "green", "orange"],
    shadow=True
)

mtp.title("Percentage of Students in Different Courses")
mtp.show()