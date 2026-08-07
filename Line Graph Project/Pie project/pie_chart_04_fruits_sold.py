import matplotlib.pyplot as mtp
import numpy as np

fruits = np.array(["Apple","Banana","Mango","Orange","Grapes"])
sold = np.array([35,25,20,10,10])

mtp.figure(facecolor="lightgray")

mtp.pie(
    sold,
    labels=fruits,
    autopct="%.2f%%",
    startangle=90,
    colors=["red","gold","orange","green","purple"]
)

mtp.title("Percentage of Fruits Sold")

mtp.show()