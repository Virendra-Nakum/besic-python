import matplotlib.pyplot as mtp
import numpy as np

course = np.array([
    "Python",
    "AI/ML",
    "Data Science",
    "Power BI",
    "SQL"
])

student = np.array([
    40,
    25,
    15,
    12,
    8
])

explode = [0.08,0.15,0,0.08,0]

color = [
    "#4CAF50",
    "#2196F3",
    "#FFC107",
    "#FF5722",
    "#9C27B0"
]

mtp.figure(figsize=(8,8), facecolor="whitesmoke")

mtp.pie(
    student,
    labels=course,
    autopct="%1.2f%%",
    colors=color,
    startangle=90,
    wedgeprops={
        "width":0.45,
        "edgecolor":"white",
        "linewidth":2
    },
    textprops={
        "fontsize":10,
        "fontweight":"bold"
    }
)

mtp.legend(title="Courses", loc="upper right")
mtp.title("Student Course Distribution", fontsize=16, fontweight="bold")
mtp.show()