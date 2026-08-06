import matplotlib.pyplot as mtp
import numpy as np

city = np.array(["jamnager","rajkot","surat","dwarka"])
population = np.array([12.4,15.3,20,15])

mtp.plot(city,population,marker='s')
mtp.gca().set_facecolor("lightblue")
mtp.title("Total Population In Gujrat")
mtp.xlabel("city name")
mtp.ylabel("poplution in lakh")
mtp.yticks([12,14,16,18,20])
mtp.legend()
mtp.show()
 