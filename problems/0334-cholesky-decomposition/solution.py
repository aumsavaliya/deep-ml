import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix.
    
    Args:
        A: A symmetric positive-definite matrix (2D list or numpy array)
    
    Returns:
        L: Lower triangular matrix such that A = L @ L.T as a 2D list,
           or -1 if decomposition is not possible
    """
    # Your code here
    A = np.array(A, dtype = float)
    if A.size == 0 or A.ndim != 2 or A.shape[0] != A.shape[1]:
        return -1
    if not np.allclose(A,A.T):
        return -1
    n = len(A)
    L = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1):
            if j == i :
                val = A[i][i] - np.dot(L[i,:i],L[i,:i])
                if val <=0:
                    return -1
                L[i][i] = np.sqrt(val)
            else:
                L[i][j] = (A[i][j] - np.dot(L[i,:j],L[j,:j]))/L[j][j]
    return L.tolist()
    