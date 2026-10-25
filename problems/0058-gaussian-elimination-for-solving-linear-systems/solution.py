import numpy as np

def gaussian_elimination(A, b):
    n = len(b)

    # forward elimination
    for i in range(n):
        # 1. pivot: find row with biggest abs value in column i (from row i down)
        r = np.argmax(abs(A[i:, i])) + i
			

        # 2. swap rows i and r in A, and also in b
        A[[i, r]] = A[[r, i]]
        b[i], b[r] = b[r], b[i]

        # 3. eliminate everything below the pivot
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]

    # back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i,i]

    return x