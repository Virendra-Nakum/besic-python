import matplotlib.pyplot as mtp

timeline = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
apple = [259.0, 264.0, 253.0, 260.0, 295.0, 315.0]
nvidia  = [191.0, 177.0, 174.0, 205.0, 235.0, 218.0]

mtp.plot(timeline,apple,marker='.',label="AAPL")
mtp.plot(nvidia,marker='o',label="NVDA")
mtp.title("Stock Price In Last 6 Month")
mtp.legend()
mtp.grid()
mtp.show()