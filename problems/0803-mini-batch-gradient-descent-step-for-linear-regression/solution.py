import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    """
    X_b = X[batch_indices]
    y_b = y[batch_indices]
    m = len(batch_indices)

    prediction = X_b.dot(weights) + bias
    error = prediction - y_b

    gradient_w = (2/m)*(X_b.T.dot(error))
    gradient_b = (2/m)*np.sum(error)

    weights = weights - lr*gradient_w
    bias = bias - lr*gradient_b

    return np.append(weights, bias) 
