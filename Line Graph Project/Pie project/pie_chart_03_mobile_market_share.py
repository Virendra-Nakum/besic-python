import matplotlib.pyplot as mtp
import numpy as np

company = np.array(["Samsung","Apple","Xiaomi","Oppo","Vivo"])
share = np.array([30,25,20,15,10])

explode = [0.1,0,0,0,0]  

mtp.figure(facecolor="lightgray")
mtp.gca().set_facecolor("lightyellow")

mtp.pie(
    share,
    labels=company,
    autopct="%.2f%%",
    explode=explode,
    shadow=True
)

mtp.title("Mobile Market Share")
mtp.show()