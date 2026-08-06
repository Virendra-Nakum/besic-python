import matplotlib.pyplot as mtp
import numpy as np

exam = np.array(["viva","test","practical","interview","que"])
marks = np.array([28,27,30,26,29])

mtp.figure(facecolor="lightgray")
mtp.plot(exam, marks, marker="s", color="b", label="Student Marks")
mtp.gca().set_facecolor("lightyellow")
mtp.title("Student Exam Marks from R_W Skill")
mtp.xlabel("Exam")
mtp.ylabel("Marks")
mtp.legend()
mtp.show()