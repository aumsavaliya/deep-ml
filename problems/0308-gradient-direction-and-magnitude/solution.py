import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	gradient = np.array(gradient, dtype = float)
	mag = np.linalg.norm(gradient)
	if mag == 0:
		direction = np.zeros_like(gradient)
	else:
		direction = gradient/mag
	
	return {
		"magnitude" : mag,
		"direction" : direction,
		"descent_direction" : -direction,
	}