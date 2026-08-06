import matplotlib.pyplot as plt

# 1. Prepare 7-Day Weekly Data (Temperature in °C)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
jamnagar_temp = [34.5, 33.0, 34.2, 33.8, 35.5, 36.1, 34.9]
mumbai_temp = [31.2, 30.8, 30.5, 32.0, 36.0, 30.5, 31.8]
 
plt.plot(days, jamnagar_temp, marker='.', color='#FF5733', linewidth=2.5, label='Jamnagar')
plt.plot(days, mumbai_temp, marker='.', color='#1F77B4', linewidth=2.5, label='Mumbai')
plt.title('Weekly Temperature Comparison')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.grid()
plt.ylim(25, 40)  
plt.legend()
 
plt.show()
