import matplotlib.pyplot as mtp
import numpy as np

Months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])


Pc=np.array([120, 135, 150, 180, 210, 290, 230, 200, 250, 280, 420, 650])
laptop=np.array([290, 170, 250, 210, 340, 420, 380, 360, 190, 410, 580, 820])

mtp.plot(Months,Pc ,marker='.',label="pc",color="g")
mtp.plot(laptop,marker='.',label="leptop",color='b')
mtp.title("Product Sales Comparison.")
mtp.xlabel("Month")
mtp.ylabel("Unit sold")
mtp.legend()
mtp.grid()
mtp.show()

 