import matplotlib.pyplot as mtp
import numpy as np

mob = np.array(["relme","apple","samsung","vivo","oppo"])
sales = np.array([2400,3100,3233,643,934])

mtp.plot(mob,sales,marker="s",label="sales by quantity")
mtp.gca().set_facecolor("lightyellow")
mtp.title("Monthly Sales Mobile In Jamnager")
mtp.xlabel("mobile")
mtp.ylabel("quantity")
mtp.legend()
mtp.show()