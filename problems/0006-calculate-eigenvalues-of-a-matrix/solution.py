def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a, b  = matrix[0]
	c, d = matrix[1]
	
	trace = a+d 
	det = a*d - b*c 

	discr= trace**2 -4*det
	sqrt_disc = discr**0.5
	l1 = (trace + sqrt_disc)/2
	l2 = (trace - sqrt_disc)/2

	return sorted([l1,l2],reverse=True)

	return eigenvalues