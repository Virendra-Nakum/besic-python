import matplotlib.pyplot as mtp
import numpy as np

web=np.array(["youtube","insta","google","chatgpt"])
vis = np.array([14.5,24,15.3,21.5])

mtp.plot(web,vis,marker='o',color="b")
mtp.title("Daliy Use Website")
mtp.xlabel("website")
mtp.ylabel("viewers")
mtp.legend()
# mtp.gca().set_facecolor("d")
mtp.show()