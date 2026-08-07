import matplotlib.pyplot as mtp
import numpy as np

expenses = np.array([12000, 8000, 5000, 3000, 2000])
category = np.array([
    "Rent",
    "Food",
    "Travel",
    "Shopping",
    "Other"
])

mtp.figure(figsize=(6,6), facecolor="lightgray")
mtp.gca().set_facecolor("lightyellow")
mtp.pie(
    expenses,
    labels=category,
    autopct="%.2f%%",
    colors=["red","blue","green","orange","pink"],
    shadow=True
)
mtp.title("Monthly Expenses")
mtp.show()