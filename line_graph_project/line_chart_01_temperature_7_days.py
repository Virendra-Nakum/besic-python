import matplotlib.pyplot as mtp
import numpy as np

tem = np.array([32,35,29,23,34,22])
day = np.array(["sun","mon","tue","thu","fri","sat"])

mtp.figure(facecolor="lightgray")
mtp.plot(day, tem, marker='o', label="Week Days", color="blue")
mtp.gca().set_facecolor("lightyellow")
mtp.title("Week Temperature in Jamnagar")
mtp.xlabel("Days")
mtp.ylabel("Temperature")
mtp.legend()
mtp.show()


 