def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    ans = c*n*(x)**(n-1)
    return ans