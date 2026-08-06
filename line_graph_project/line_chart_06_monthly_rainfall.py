import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [0.4, 0.1, 0.6, 1.1, 0.0, 125.0, 248.0, 175.0, 65.0, 5.0, 1.5, 0.5]

plt.figure(figsize=(10, 6))
plt.plot(months, rainfall, marker='o', color='#1f77b4', linestyle='-', linewidth=2.5, label='Rainfall (mm)')
plt.title('Average Monthly Rainfall in Jamnagar, Gujarat', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=12, labelpad=10)
plt.ylabel('Rainfall (mm)', fontsize=12, labelpad=10)
plt.grid(True, linestyle='--', alpha=0.5)   
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('jamnagar_monthly_rainfall.png', dpi=300)
plt.show()
