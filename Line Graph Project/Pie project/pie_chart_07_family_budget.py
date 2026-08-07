import matplotlib.pyplot as mtp
import numpy as np

budget = np.array(["House Rent","Food","Education","Travel","Savings"])
amount = np.array([25000,12000,8000,5000,10000])

explode = [0.08,0,0.08,0,0]

mtp.figure(facecolor="mintcream")

mtp.pie(
    amount,
    labels=budget,
    autopct="%1.2f%%",
    explode=explode,
    startangle=90,
    colors=["royalblue","gold","limegreen","tomato","violet"],
    shadow=True
)

mtp.legend(title="Budget")
mtp.title("Family Budget Distribution")

mtp.show()