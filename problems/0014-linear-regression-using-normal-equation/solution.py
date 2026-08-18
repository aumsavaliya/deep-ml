import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X = np.array(X, dtype = float)
	y = np.array(y, dtype = float)
	X_T = X.T
	theta = np.linalg.inv(X_T @ X) @ X_T @ y
	
	theta = np.round(theta, 4)
	return theta.tolist()
