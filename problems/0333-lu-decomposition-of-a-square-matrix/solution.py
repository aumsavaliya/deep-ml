import numpy as np

def lu_decomposition(A: list) -> tuple:
	"""
	Perform LU decomposition on a square matrix using Doolittle's method.
	
	Args:
		A: Square matrix as a list of lists
	
	Returns:
		tuple: (L, U) where L is lower triangular with 1s on diagonal,
		       U is upper triangular, and A = L @ U
	"""
	# Your code here
	A = np.array(A, dtype=float)
	n = len(A)
	L = np.zeros((n,n)) 
	U = np.zeros((n,n))
	for i in range(n):
		for k in range(i,n):
			U[i][k] = A[i][k] - np.dot(L[i,:i],U[:i,k])
		for k in range(i,n):
			if k == i :
				L[i][i] = 1
			else :
				L[k][i] = (A[k][i] - np.dot(L[k,:i], U[:i,i])) / U[i][i]

	return L,U
	