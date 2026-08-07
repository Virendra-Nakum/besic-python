import matplotlib.pyplot as mtp
import numpy as np

browser = np.array(["Chrome","Edge","Firefox","Safari","Opera"])
users = np.array([55,20,12,8,5])

explode = [0.1,0,0,0,0]

mtp.figure(facecolor="lavender")

mtp.pie(
    users,
    labels=browser,
    autopct="%1.2f%%",
    explode=explode,
    pctdistance=0.75,
    colors=["gold","deepskyblue","orange","limegreen","violet"],
    shadow=True
)

mtp.title("Browser Usage Percentage")

mtp.show()
