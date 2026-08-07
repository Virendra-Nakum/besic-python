import matplotlib.pyplot as mtp
import numpy as np

candidate = np.array(["Rahul","Amit","Karan","Riya","Neha"])
votes = np.array([420,310,260,180,130])

mtp.figure(facecolor="lightcyan")

mtp.pie(
    votes,
    labels=candidate,
    autopct="%1.0f%%",
    colors=["skyblue","gold","lightgreen","tomato","violet"],
    shadow=True,
    counterclock=False
)

mtp.title("Votes Received by Candidates")

mtp.show()