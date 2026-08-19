import math
import numpy as np

PI = 3.14159

def power_grid_forecast(data):
	# 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
	# 2) Perform linear regression on the detrended data.
	# 3) Predict day 15's base consumption.
	# 4) Add the day 15 fluctuation back.
	# 5) Round, then add a 5% safety margin (rounded up).
	# 6) Return the final integer.


	days = np.arange(1,11)
	fluctuation = 10*np.sin(2*np.pi*days/10)
	detrended = np.array(data)- fluctuation

	m, c = np.polyfit(days,detrended,1)

	day15_base = m*15 +c 
	day15_fluctuation = 10*np.sin(2*np.pi*15/10)
	day15_total = day15_base + day15_fluctuation

	rounded_total = round(day15_total)
	final = math.ceil(rounded_total*1.05)
	return final 
	