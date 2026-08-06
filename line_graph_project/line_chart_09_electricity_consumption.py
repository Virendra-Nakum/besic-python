import matplotlib.pyplot as mtp
 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
house_a = [180, 260, 250, 210, 290, 380, 420, 390, 310, 240, 250, 300]
house_b = [750, 720, 250, 360, 480, 590, 650, 910, 607, 390, 410, 680]

mtp.plot(months,house_a,color='y',label="house A",marker='.')
mtp.plot(house_b,color='g',label="house B",marker='.')
mtp.title("Annual Electricity Consumption Comparison")
mtp.xlabel("Month")
mtp.ylabel("House Billes ")
mtp.legend()
mtp.grid()
mtp.show()
