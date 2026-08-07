import matplotlib.pyplot as mtp
import numpy as np

brand = np.array([
    "Nike",
    "Adidas",
    "Puma",
    "Reebok",
    "Campus"
])

sales = np.array([
    320,
    260,
    180,
    120,
    90
])

explode = [
    0.15,
    0.08,
    0.12,
    0.05,
    0.10
]

mtp.figure(facecolor="lavender")

mtp.pie(
    sales,
    labels=brand,
    autopct="%1.2f%%",
    colors=["gold","blue","green","orange","purple"],
    shadow=True,
    startangle=1
)

mtp.title("Brand Sales Distribution (Exploded Pie Chart)")

mtp.show()