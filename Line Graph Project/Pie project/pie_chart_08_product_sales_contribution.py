import matplotlib.pyplot as mtp
import numpy as np

product = np.array(["Laptop","Mobile","Tablet","Smart Watch","Headphone"])
sales = np.array([450,320,180,120,80])

mtp.figure(facecolor="aliceblue")

mtp.pie(
    sales,
    labels=product,
    autopct="%1.2f%%",
    colors=["dodgerblue","orange","limegreen","violet","red"],
    shadow=True,
    wedgeprops={"width":0.45,"edgecolor":"white"}
)

mtp.title("Product Sales Contribution")

mtp.show()